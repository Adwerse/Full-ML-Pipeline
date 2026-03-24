# Full-ML-Pipeline

Production-ready language detection API built with FastAPI, containerized with Docker, and deployed on Railway.

## Live Demo 🚀

- UI: https://full-ml-pipeline-production.up.railway.app/ui
- Health check: https://full-ml-pipeline-production.up.railway.app/
- API docs (Swagger): https://full-ml-pipeline-production.up.railway.app/docs

## Features ✨

- Language prediction endpoint for user text
- Clean web UI for manual testing
- FastAPI OpenAPI documentation
- Dockerized deployment flow
- Railway hosting support

## Project Structure

```text
.
├── Dockerfile
├── README.md
└── app
    ├── main.py
    ├── requirements.txt
    ├── static
    │   └── index.html
    └── model
        ├── model.py
        ├── trained_pipeline-0.1.0.pkl
        └── LangDetetctionModel.ipynb
```

## API 🤖

### GET /
Returns service status and model version.

Example response:

```json
{
  "health_check": "OK",
  "model_version": "0.1.0"
}
```

### GET /ui
Serves the web interface for submitting text and viewing predictions.

### POST /predict
Predicts the language of the provided text.

Request body:

```json
{
  "text": "Bonjour, comment allez-vous aujourd'hui?"
}
```

Response:

```json
{
  "language": "French"
}
```

## Run Locally (Docker)

Build image:

```bash
docker build -t language-detection-app .
```

Run container:

```bash
docker run --rm -p 80:80 language-detection-app
```

Open in browser:

- http://localhost/ui
- http://localhost/docs

## Quick Test with curl

```bash
curl -X POST "http://localhost/predict" \
  -H "Content-Type: application/json" \
  -d '{"text":"Hello, how are you today?"}'
```

## Deployment Notes

- Hosted on Railway using the repository Dockerfile.
- For lower startup overhead on small instances, worker settings can be tuned with:
  - WEB_CONCURRENCY=1
  - MAX_WORKERS=1

## Tech Stack

- Python 3.9
- FastAPI
- scikit-learn
- NumPy
- Docker
- Railway

## Author

Adam Vakar
