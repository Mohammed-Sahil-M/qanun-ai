from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Qanun AI"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # API Keys
    GROQ_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    
    # RAG Settings
    CHROMA_DB_DIR: str = "./chroma_db"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    LLM_MODEL: str = "llama-3.3-70b-versatile"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
