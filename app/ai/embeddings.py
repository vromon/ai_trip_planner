from app.config import settings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
def get_embedding_function()->GoogleGenerativeAIEmbeddings:
    return GoogleGenerativeAIEmbeddings(
    google_api_key=settings.GEMINI_API, 
    model="models/gemini-embedding-001",
    output_dimensionality=1024
)