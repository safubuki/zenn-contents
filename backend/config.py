"""
Configuration module for Robot Agent System API.
Phase 1 implementation with basic environment variable support.
Phase 2 will use pydantic-settings for advanced configuration management.
"""

import os
from typing import List


class Settings:
    """Basic settings class for Phase 1."""
    
    def __init__(self):
        # Google Cloud API Configuration
        self.google_api_key: str = os.getenv("GOOGLE_API_KEY", "")
        
        # Server Configuration
        self.host: str = os.getenv("HOST", "0.0.0.0")
        self.port: int = int(os.getenv("PORT", "8000"))
        self.debug: bool = os.getenv("DEBUG", "True").lower() == "true"
        
        # CORS Configuration
        cors_origins_env = os.getenv("CORS_ORIGINS", "http://localhost:3000,http://localhost:8080")
        self.cors_origins: List[str] = [origin.strip() for origin in cors_origins_env.split(",")]
        
        # ChromaDB Configuration (for Phase 2)
        self.chroma_persist_directory: str = os.getenv("CHROMA_PERSIST_DIRECTORY", "./chroma_db")
        self.chroma_collection_name: str = os.getenv("CHROMA_COLLECTION_NAME", "robot_commands")
        
        # LangChain Configuration (for Phase 2)
        self.langchain_tracing_v2: bool = os.getenv("LANGCHAIN_TRACING_V2", "False").lower() == "true"
        self.langchain_endpoint: str = os.getenv("LANGCHAIN_ENDPOINT", "https://api.smith.langchain.com")
        self.langchain_api_key: str = os.getenv("LANGCHAIN_API_KEY", "")
        self.langchain_project: str = os.getenv("LANGCHAIN_PROJECT", "robot-agent-system")


# Global settings instance
settings = Settings()