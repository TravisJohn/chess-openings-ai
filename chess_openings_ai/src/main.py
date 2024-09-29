from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from api.routes import router as api_router
from rag_pipeline.pipeline import RAGPipeline
import os

app = FastAPI()

# Include the API router with the "/api" prefix
app.include_router(api_router, prefix="/api")

# Add a root route directly in main.py
@app.get("/")
async def root():
    return {"message": "Welcome to Chess Openings AI"}

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"An unexpected error occurred: {str(exc)}"},
    )

def main():
    gemini_api_key = os.getenv('GEMINI_API_KEY')
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")

    pipeline = RAGPipeline(gemini_api_key)
    pipeline.setup()

    while True:
        query = input("Enter your chess opening query (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        results = pipeline.query(query)
        print(results)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)