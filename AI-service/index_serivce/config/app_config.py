from pydantic_settings import BaseSettings
from pydantic import Field


class AppConfig(BaseSettings):
    
    persist_dir: str = Field(..., env="PERSIST_DIR")
    num_file_limit: int = Field(..., env="NUM_FILE_LIMIT")
    graph_db_url: str = Field(..., env="GRAPH_DB_URL")
    graph_db_user: str = Field(..., env="GRAPH_DB_USER")
    graph_db_password: str = Field(..., env="GRAPH_DB_PASSWORD")
    graph_db_database_name: str = Field(..., env="GRAPH_DB_DATABASE_NAME")
    qdrant_address: str = Field(..., env="QDRANT_ADDRESS")
    qdrant_port: int = Field(..., env="QDRANT_PORT")
    minio_endpoint: str = Field(..., env="MINIO_ENDPOINT")
    minio_access_key: str = Field(..., env="MINIO_ACCESS_KEY")
    minio_secret_key: str = Field(..., env="MINIO_SECRET_KEY")
    minio_secure: bool = Field(..., env="MINIO_SECURE")
    host_url: str = Field(..., env="HOST_URL")
    host_port: int = Field(..., env="HOST_PORT")
    url_local_ollama: str = Field(..., env="URL_LOCAL_OLLAMA")
    
    class Config:
        env_file = "./AI-service/index_serivce/.env.dev"
        env_file_encoding = "utf-8"
        extra="allow"

settings = AppConfig()
