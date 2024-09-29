import chromadb
from chromadb.config import Settings

class ChromaVectorStore:
    def __init__(self, persist_directory="./data/chroma_db"):
        self.client = chromadb.Client(Settings(
            chroma_db_impl="duckdb+parquet",
            persist_directory=persist_directory
        ))
        self.collection = self.client.get_or_create_collection("chess_openings")

    def add_documents(self, documents, metadatas, ids):
        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    def query(self, query_text, n_results=3):
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )