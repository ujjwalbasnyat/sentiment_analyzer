# Sentiment Analyzer

A Python-based sentiment analysis tool that processes text data to determine sentiment polarity (positive, negative, or neutral).

## Features

- Analyzes sentiment of input text
- Supports batch processing of datasets
- Provides sentiment scores and classifications
- Easy integration with other Python projects

## Installation

```bash
git clone https://github.com/yourusername/sentiment-analyzer.git
cd sentiment-analyzer
pip install -r requirements.txt
```

## Usage

```python
from sentiment_analyzer import analyze_sentiment

result = analyze_sentiment("I love this product!")
print(result)  # Output: {'sentiment': 'positive', 'score': 0.85}
```

## Running Locally

This project uses FastAPI for serving the sentiment analysis API. To run the application locally:

```bash
uvicorn sentiment_analyzer.main:app --reload --port 8000
```

The API will be available at [http://localhost:8000](http://localhost:8000).

## Using Swagger UI

Once the server is running, you can access the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

To send a POST request for sentiment analysis in Swagger UI:

1. Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.
2. Find the `/analyze` POST endpoint.
3. Click "Try it out".
4. Enter your input text in the request body, for example:
    ```json
    {
      "text": "I love this product!"
    }
    ```
5. Click "Execute" to see the sentiment analysis result.

The default running port is **8000**. You can change it by modifying the `--port` parameter in the `uvicorn` command.

## Project Structure

```
sentiment-analysis/
├── sentiment_analyzer/
│   └── __init__.py
├── tests/
├── requirements.txt
└── readme.md
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.

## 12-Factor App Principles

This project follows several 12-Factor App principles:

- **Codebase:** Maintained in a single, version-controlled repository.
- **Dependencies:** All dependencies are declared in `requirements.txt`.
- **Configuration:** Configuration can be managed via environment variables for flexibility.
- **Backing Services:** Easily integrates with external services (e.g., databases, APIs) as attachable resources.
- **Dev/Prod Parity:** Consistent environments for development and production through dependency management.
- **Logs:** Outputs logs to stdout/stderr, making it compatible with log aggregation tools.

For more information on the 12-Factor App methodology, visit [12factor.net](https://12factor.net/).
