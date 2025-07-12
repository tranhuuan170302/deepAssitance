from minio import Minio
from fastapi import UploadFile
from typing import Optional, List
import uuid
import io

class RepositoryMinio:

    def __init__(self, minio_client: Minio):
        self.minio_client = minio_client

    def upload_file(self, file: List[UploadFile], bucket_name: str, object_name: Optional[str] = None) -> bool:
        try:
            if not self.minio_client.bucket_exists(bucket_name):
                self.minio_client.make_bucket(bucket_name)
            else:
                return False
            for f in file:
                data = f.file.read()
                self.minio_client.put_object(
                    bucket_name=bucket_name,
                    object_name=uuid.uuid4().hex,
                    data=io.BytesIO(data),
                    length=len(data),
                    content_type=f.content_type or "application/octet-stream"
                )
            return True
        except Exception as e:
            raise e
