from index_serivce.infra.db.qdrant_client import qdrant_client
from llama_index.vector_stores.qdrant import QdrantVectorStore
from index_serivce.infra.repository.repository_qdrant import VectorStoreIndex
from llama_index.core import Document
from llama_index.core import StorageContext
from llama_index.embeddings.ollama import OllamaEmbedding
from typing import List
import multiprocessing
from index_serivce.config.app_config import settings

class BuildIndexService:
    def __init__(self):
        self.qdrant_client, self.as_qdrant_client = qdrant_client()
        self.optimal_parallel = max(3, multiprocessing.cpu_count() // 2)
        self.embedding_model = OllamaEmbedding(
            model_name="bge-m3:latest",
            base_url=settings.url_local_ollama
        )
    
    def build_index(self, collection_name: str, documents: List[str]):
        vector_store = QdrantVectorStore(
            client=self.qdrant_client,
            aclient=self.as_qdrant_client,
            parallel=self.optimal_parallel,
            collection_name=collection_name
        )
        storage_context = StorageContext.from_defaults(
            vector_store=vector_store
        )
        doc_objects = [Document(text=doc) for doc in documents]
        VectorStoreIndex.from_documents(
            documents=doc_objects,
            storage_context=storage_context,
            embed_model=self.embedding_model,
            show_progress=True,
        )
        self.qdrant_client.delete_collection("chunks")
        self.qdrant_client.delete_collection("entities")
        self.qdrant_client.delete_collection("relationships")
        return "yes oke true"

    def retrivel(self, collection_name: str):
        pass

build_index_service = BuildIndexService()