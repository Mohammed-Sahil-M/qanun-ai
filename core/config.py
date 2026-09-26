import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Qanun AI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # RAG Settings
    CHROMA_DB_DIR: str = "./chroma_db"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    LLM_MODEL: str = "llama-3.3-70b-versatile"
    
    class Config:
        env_file = ".env"

settings = Settings()
