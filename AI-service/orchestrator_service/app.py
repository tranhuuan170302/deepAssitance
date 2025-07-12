from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.runnables import RunableConfig
from sse_startletter.sse import EnventSourceResponse



runnable_config = RunnableConfig(recursion_limit=50)


# def unregister(server_id: str):
#     request.delete()


def register():

    server_info = 