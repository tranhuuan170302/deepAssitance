from typing import Optional
from index_serivce.infra.repository.repository_minio import RepositoryMinio
from fastapi import UploadFile


class UploadService:
    def __init__(self, repository_minio: RepositoryMinio):
        self.repository_minio = repository_minio
    
    def upload_file(self, file: UploadFile, bucket_name: str, object_name: Optional[str] = None) -> bool:
        return self.repository_minio.upload_file(file, bucket_name, object_name)