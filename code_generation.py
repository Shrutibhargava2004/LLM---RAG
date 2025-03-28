import chromadb
from sentence_transformers import SentenceTransformer
import inspect


def retrieve_function(user_query):
    # Specify the database location
    persist_directory = "D:/interns/LLM + RAG/chroma_db"
    client = chromadb.PersistentClient(path=persist_directory)

    # Load the collection
    collection = client.get_or_create_collection(name="function_metadata")

    # Load the Sentence Transformer model
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # Generate embedding for the user query
    query_embedding = model.encode([user_query]).tolist()

    # Perform similarity search using ChromaDB
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=1
    )

    if results["ids"] and results["metadatas"]:
        function_data = results["metadatas"][0][0]
        print("Most Relevant Function Found:")
        print(f"Function Name: {function_data['name']}")
        print(f"Description: {function_data['description']}")
        print(f"Module: {function_data['module']}")

        # Dynamically import the module and retrieve the function
        module = __import__(function_data['module'])
        function = getattr(module, function_data['name'])

        # Display the function definition
        function_code = inspect.getsource(function)
        print("\nFunction Definition:")
        print(function_code)

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
        print("\nGenerated Code:")
        print(generated_code)
    else:
        print("No matching function found.")


if __name__ == "__main__":
    user_query = input("Enter your query: ")
    retrieve_function(user_query)
