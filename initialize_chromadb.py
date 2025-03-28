import chromadb
from sentence_transformers import SentenceTransformer
from function_metadata import function_metadata

def initialize_chromadb():
    # Specify your custom directory to store the database
    persist_directory = "D:/interns/LLM + RAG/chroma_db"
    client = chromadb.PersistentClient(path=persist_directory)

    # Create or get a collection
    collection = client.get_or_create_collection(name="function_metadata")

    # Load Sentence Transformer model for embedding generation
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

    # Process and store function metadata with embeddings
    descriptions = [func['description'] for func in function_metadata]
    embeddings = model.encode(descriptions).tolist()

    for i, func in enumerate(function_metadata):
        collection.add(
            ids=[str(i)],
            embeddings=[embeddings[i]],
            metadatas=[func]
        )
    
    print("Function metadata stored successfully!")
    print(f"Database is stored at: {persist_directory}")

if __name__ == "__main__":
    initialize_chromadb()
