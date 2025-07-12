from fastapi import APIRouter, Depends
from fastapi import UploadFile, File, Form
from typing import Optional, List
from index_serivce.application.models.response import HealthyCheckResponse, UploadFileResponse
from index_serivce.application.services.services import system_service
from index_serivce.infra.db.minio_client import minio_client
from index_serivce.application.services.buildIndex_service import build_index_service
# create router for service index
index_router = APIRouter(prefix="/v1")


@index_router.get("/healthy", response_model=HealthyCheckResponse)
async def healthy_check(
        minio_client: minio_client = Depends(minio_client)
    ):

    return system_service.check_healthy(minio_client)


@index_router.post("/upload", response_model=UploadFileResponse)
async def upload_file(file: List[UploadFile] = File(...), 
                    bucket_name: str = Form(...), 
                    object_name: Optional[str] = Form(...)):

    return system_service.upload_file(file, bucket_name, object_name)

@index_router.post("/build-index")
async def build_index(collection_name: str, documents: List[str]):
    return build_index_service.build_index(collection_name, documents)
