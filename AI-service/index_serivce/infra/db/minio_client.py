from minio import Minio
from minio.error import S3Error
from index_serivce.config.app_config import settings

def minio_client():
    return Minio(
        endpoint=settings.minio_endpoint,
        access_key=settings.minio_access_key,
        secret_key=settings.minio_secret_key,
        secure=settings.minio_secure
)
