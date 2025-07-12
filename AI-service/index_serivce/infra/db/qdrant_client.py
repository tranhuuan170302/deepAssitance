from qdrant_client import QdrantClient, AsyncQdrantClient
from index_serivce.config.app_config import settings

def qdrant_client():
    qdrant_client = QdrantClient(
        host=settings.qdrant_address,
        port=settings.qdrant_port,
    )

    as_qdrant_client = AsyncQdrantClient(
        host=settings.qdrant_address,
        port=settings.qdrant_port,
    )

    return qdrant_client, as_qdrant_client
