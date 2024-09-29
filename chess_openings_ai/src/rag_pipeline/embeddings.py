import google.generativeai as genai
from chromadb.utils import embedding_functions

class GeminiEmbeddingFunction(embedding_functions.EmbeddingFunction):
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def __call__(self, texts):
        embeddings = []
        for text in texts:
            response = self.model.generate_content(text)
            embeddings.append(response.text)  # Adjust based on actual Gemini API response
        return embeddings