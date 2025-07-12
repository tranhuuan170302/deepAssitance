import time
from fastapi import UploadFile
from datetime import datetime
from index_serivce.application.models.response import HealthyCheckResponse, UploadFileResponse
from index_serivce.application.services.upload_service import UploadService
from index_serivce.infra.repository.repository_minio import RepositoryMinio
from index_serivce.infra.db.minio_client import minio_client

class CheckSystemCheckSystem:

    def __init__(self):
        self.status_overview = None
        self.information_connection_data = {}
        self.upload_service = UploadService(RepositoryMinio(minio_client()))
    
    def check_healthy(self, minio_client: minio_client) -> HealthyCheckResponse:
        start_time = time.time()
        
        if minio_client:
            self.status_overview = "ok"
            print(f"minio client: {minio_client.list_buckets()}")
            self.information_connection_data = {
                "minio": "ok"
            }
        else:
            self.status_overview = "error"
            self.information_connection_data = {
                "minio": "error"
            }
        
        end_time = time.time()
        
        return HealthyCheckResponse(
            status=self.status_overview,
            time_stamp=datetime.now().isoformat(),
            uptime_seconds=end_time - start_time,
            version="1.0.0",
            env="development",
            hostname="localhost:8000",
            details=self.information_connection_data
        )

    def upload_file(self, file: UploadFile, bucket_name: str, object_name: str = None) -> bool:
        print(self.status_overview)
        if self.status_overview == "ok":
            if self.upload_service.upload_file(file, bucket_name, object_name):
                return UploadFileResponse(
                    status="oke",
                    message="upload success",
                    time_stamp=datetime.now().isoformat(),
                    code="ULUL200"
                )
            else:
                return UploadFileResponse(
                    status="error",
                    message="upload failed",
                    time_stamp=datetime.now().isoformat(),
                    code="UL301UL301"
                )
        else:
            return UploadFileResponse(
                status="error",
                message="can not access",
                time_stamp=datetime.now().isoformat(),
                code="UL500"
            )


system_service = CheckSystemCheckSystem()
