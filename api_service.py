from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import chromadb
from sentence_transformers import SentenceTransformer
import inspect
import importlib
from fastapi.responses import JSONResponse

app = FastAPI()

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Load ChromaDB and Sentence Transformer
persist_directory = "D:/interns/LLM + RAG/chroma_db"
client = chromadb.PersistentClient(path=persist_directory)
collection = client.get_or_create_collection(name="function_metadata")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Input models
class QueryRequest(BaseModel):
    prompt: str

class ExecuteRequest(BaseModel):
    function_name: str

# Home route to display the frontend
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# API endpoint to retrieve and generate function code
@app.post("/execute")
def execute_function(request: QueryRequest):
    user_query = request.prompt

    # Generate embedding for the user query
    query_embedding = model.encode([user_query]).tolist()

    # Perform similarity search using ChromaDB
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=1
    )

    if results["ids"] and results["metadatas"]:

        function_data = results["metadatas"][0][0]

        try:
            # Dynamically import module and get function definition
            module = importlib.import_module(function_data['module'])
            function = getattr(module, function_data['name'])
            function_code = inspect.getsource(function)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error retrieving function code: {e}")

        # Generate Python code for function execution
        generated_code = f"""
from {function_data['module']} import {function_data['name']}

def main():
    try:
        {function_data['name']}()
        print("Function executed successfully.")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
"""
        return JSONResponse(content={
            "function": function_data['name'],
            "description": function_data['description'],
            "code": generated_code,
            "function_definition": function_code
        })
    else:
        raise HTTPException(status_code=404, detail="No matching function found.")

@app.post("/run")
def run_function(request: ExecuteRequest):
    function_name = request.function_name

    try:
        # Retrieve function data using the function name
        collection_results = collection.get(where={"name": function_name})
        if not collection_results['metadatas']:
            raise HTTPException(status_code=404, detail="Function not found in the collection.")
        
        function_data = collection_results['metadatas'][0]
        module = importlib.import_module(function_data['module'])
        function_to_execute = getattr(module, function_name)
        
        # Execute the function and capture the output
        output = function_to_execute()

        if output is None:
            return JSONResponse(content={"message": f"Function '{function_name}' executed successfully but did not return any output."})
        else:
            return JSONResponse(content={"message": f" {output}"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error executing function: {e}")
