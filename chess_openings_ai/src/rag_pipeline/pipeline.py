from .document_loader import get_chess_openings_data
from .vector_store import ChromaVectorStore
from .embeddings import GeminiEmbeddingFunction

class RAGPipeline:
    def __init__(self, gemini_api_key):
        self.chess_openings = get_chess_openings_data()
        self.vector_store = ChromaVectorStore()
        self.embedding_function = GeminiEmbeddingFunction(gemini_api_key)

    def setup(self):
        documents = [opening['content'] for opening in self.chess_openings]
        metadatas = [opening['metadata'] for opening in self.chess_openings]
        ids = [opening['id'] for opening in self.chess_openings]
        
        self.vector_store.add_documents(documents, metadatas, ids)

    def query(self, query_text, n_results=3):
        return self.vector_store.query(query_text, n_results)