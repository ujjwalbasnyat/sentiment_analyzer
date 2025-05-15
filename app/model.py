from transformers import pipeline

#Load model only once
sentiment_pipeline = pipeline("sentiment-analysis")


def predict_sentiment(text: str) -> str:
    result = sentiment_pipeline(text)[0]
    return result['label'].lower()