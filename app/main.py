import os
import socket
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "hello from azure container apps",
        "version": os.getenv("APP_VERSION", "dev"),
        "hostname": socket.gethostname(),
    }

@app.get("/health")
def health():
    return {"status": "ok"}