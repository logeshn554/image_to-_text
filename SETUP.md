# Local Development Setup

## Prerequisites
- Python 3.11+
- Node.js 18+
- 4GB+ RAM (for BLIP model)

## Backend Setup

1. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Configure environment (optional)**
   ```bash
   cp .env.example .env
   # Default settings work for local development
   ```

3. **Start the server**
   ```bash
   uvicorn app.main:app --reload
   ```

   API runs on: http://localhost:8000

## Frontend Setup

1. **Install dependencies**
   ```bash
   cd frontend
   npm install
   ```

2. **Configure environment (optional)**
   ```bash
   cp .env.example .env
   # Update VITE_API_URL if backend is on different host/port
   ```

3. **Start dev server**
   ```bash
   npm run dev
   ```

   Frontend runs on: http://localhost:5176 (or next available port)

## Usage

1. Open http://localhost:5176 in your browser
2. Upload an image (drag & drop or click)
3. Click "Generate Caption"
4. Wait for BLIP model to download on first run (~30 seconds)
5. View generated caption

## API

Generate captions programmatically:

```bash
curl -X POST -F "file=@image.jpg" http://localhost:8000/generate-caption
```

Response:
```json
{
  "caption": "a dog playing in the park"
}
```

## Environment Variables

### Backend (.env)
- `CORS_ORIGINS` - Comma-separated CORS origins (default: localhost)
- `MODEL_NAME` - Hugging Face model ID
- `MAX_IMAGE_SIZE_MB` - Max upload size in MB

### Frontend (.env)
- `VITE_API_URL` - Backend API URL (default: http://localhost:8000)

## Troubleshooting

**CORS errors in browser console**
- Solution: Add frontend URL to `CORS_ORIGINS` in `backend/.env`

**Port already in use**
- Backend: `uvicorn app.main:app --reload --port 9000`
- Frontend: `npm run dev -- --port 3000`

**BLIP model download stuck**
- The model downloads on first image upload (~350MB)
- Requires 4GB+ free RAM
- Be patient, can take 30-60 seconds on first run

## Production Deployment

```bash
# Build frontend
cd frontend && npm run build

# Run backend
cd backend
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

No external services (database, etc.) required!

