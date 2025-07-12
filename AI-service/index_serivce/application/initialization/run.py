from fastapi import FastAPI
from index_serivce.application.presentation.rest.api import index_router
from fastapi.middleware.cors import CORSMiddleware

# initliazation for App
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include router
app.include_router(index_router)
