from pydantic import BaseModel


class HealthyCheckResponse(BaseModel):
    status: str
    time_stamp: str
    uptime_seconds: float
    version: str
    env: str
    hostname: str
    details: dict


class UploadFileResponse(BaseModel):
    status: str
    message: str
    time_stamp: str
    code: str