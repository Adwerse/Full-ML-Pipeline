from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version
from pathlib import Path


app = FastAPI()
STATIC_DIR = Path(__file__).resolve().parent / "static"


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.get("/ui")
def ui():
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    language = predict_pipeline(payload.text)
    return {"language": language}