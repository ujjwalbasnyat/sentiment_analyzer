from fastapi import FastAPI
from pydantic import BaseModel
from app.model import predict_sentiment

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.post("/")
def health_check():
    return {"status": "ok"}

@app.post("/analyze")
def analyze(input_text: InputText):
    sentiment = predict_sentiment(input_text.text)
    return {"sentiment": sentiment}