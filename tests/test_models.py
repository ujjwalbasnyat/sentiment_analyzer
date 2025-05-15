from app.model import predict_sentiment

def test_positive_sentiment():
    assert predict_sentiment("I love this product!") == "positive"

def test_negative_sentiment():
    assert predict_sentiment("I hate bugs!") == "negative"