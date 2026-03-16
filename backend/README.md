# Image Caption Generator Backend

FastAPI backend that generates text captions from images using the BLIP model. No database required - stateless API.


## Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Server runs on: http://localhost:8000

API Documentation: http://localhost:8000/docs

## API Endpoints

- `POST /generate-caption` - Generate caption from image
  - Body: form-data with `file` field (image)
  - Returns: `{"caption": "text description"}`

- `GET /health` - Server health check
  - Returns: `{"status": "ok", "version": "1.0.0", "model": "BLIP"}`


## Configuration

Set via environment variables in `.env`:

- `CORS_ORIGINS` - Comma-separated CORS allowed origins (default: localhost)
- `MODEL_NAME` - Hugging Face model ID (default: Salesforce/blip-image-captioning-base)
- `MAX_IMAGE_SIZE_MB` - Max upload size in MB (default: 10)


## Model

Uses Salesforce BLIP for image captioning:
- Model: `Salesforce/blip-image-captioning-base`
- Downloads on first use (~350MB)
- GPU acceleration supported (auto-detected)

