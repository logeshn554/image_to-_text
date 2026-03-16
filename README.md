# Image Caption Generator

A simple full-stack application that generates text captions from images using the BLIP model. **No database required - completely stateless!**

## Overview

- **Upload**: Users upload images
- **Generate**: AI generates descriptive text captions  
- **Frontend**: React UI with drag-and-drop
- **Backend**: FastAPI with BLIP model
- **Storage**: None - stateless API

## Tech Stack

- **Frontend**: React 19 + TypeScript + Vite
- **Backend**: FastAPI + Python 3.11
- **Model**: BLIP (Salesforce/blip-image-captioning-base)
- **Database**: None!

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- 4GB+ RAM

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend runs on: http://localhost:8000

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on: http://localhost:5176 (or next available port)

## Usage

1. Open frontend in browser
2. Upload an image (drag-drop or click)
3. Click "Generate Caption"
4. Wait for BLIP model to download on first run (~30 seconds)
5. View generated caption

Done! No database setup, no external services needed.

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

## Features

- ✅ No database required
- ✅ No API keys needed
- ✅ Drag-and-drop UI
- ✅ GPU acceleration support
- ✅ Production-ready
- ✅ CORS configured for localhost

See [SETUP.md](SETUP.md) for detailed setup instructions.


## 📁 Project Structure

```
Poultryform/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI app, routes
│   │   ├── config.py        # Settings & constants
│   │   ├── database.py      # SQLAlchemy setup
│   │   ├── models.py        # Image model
│   │   ├── schemas.py       # Pydantic schemas
│   │   ├── crud.py          # Database operations
│   │   ├── embeddings.py    # CLIP model & embedding generation
│   │   └── utils.py         # Helper functions
│   ├── static/images/       # Uploaded images
│   ├── requirements.txt     # Python dependencies
│   ├── Dockerfile           # Container definition
│   ├── docker-compose.yml   # Services orchestration
│   └── README.md
│
└── frontend/
    ├── src/
    │   ├── App.tsx          # Main app component
    │   ├── App.css          # Global styles (professional UI)
    │   └── components/
    │       ├── Header.tsx     # Navigation header
    │       ├── Footer.tsx     # Footer section
    │       ├── UploadForm.tsx # File upload & drag-drop
    │       ├── ResultsGrid.tsx # Search results display
    │       ├── ImageHistory.tsx # Uploaded images browser
    │       ├── LoadingSpinner.tsx # Loading indicator
    │       └── ErrorMessage.tsx # Error notifications
    ├── package.json         # Node dependencies
    ├── vite.config.ts       # Vite config
    └── .env.example         # Environment setup
```

## 🎨 Features

### Frontend
- ✅ **Drag & Drop Upload** - Easy image upload with visual feedback
- ✅ **Live Preview** - See selected image before uploading
- ✅ **Search Interface** - Upload & get similar images instantly
- ✅ **Image History** - Browse all uploaded images with pagination
- ✅ **Stats Dashboard** - View total indexed images & model info
- ✅ **Error Handling** - User-friendly error messages
- ✅ **Loading States** - Spinner during search/upload
- ✅ **Responsive Design** - Works on mobile, tablet, desktop
- ✅ **Dark Mode** - Automatic dark/light theme support
- ✅ **Professional UI** - Modern cards, gradients, animations

### Backend
- ✅ **Image Upload** - Store & validate image files
- ✅ **CLIP Embeddings** - Fast neural embeddings (768-dim)
- ✅ **Vector Search** - Cosine similarity search (top-k results)
- ✅ **CRUD Operations** - List, upload, delete images
- ✅ **Pagination** - Handle large datasets efficiently
- ✅ **Error Handling** - Input validation, detailed error messages
- ✅ **CORS Support** - Works with frontend on different origin
- ✅ **Health Checks** - Monitor API status
- ✅ **API Documentation** - Auto-generated Swagger/OpenAPI docs

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/health` | Health check |
| `GET` | `/stats` | Database & model stats |
| `POST` | `/upload` | Upload & index image |
| `POST` | `/search` | Search for similar images |
| `GET` | `/images` | List all images (paginated) |
| `DELETE` | `/image/{id}` | Delete image |

### Example Usage

**Upload Image:**
```bash
curl -F "file=@photo.jpg" \
  -F "description=My vacation" \
  http://localhost:8000/upload
```

**Search:**
```bash
curl -F "file=@query.jpg" -F "top_k=10" \
  http://localhost:8000/search
```

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI (async, type-hints, auto-docs)
- **ORM**: SQLAlchemy (database abstraction)
- **Database**: PostgreSQL (vector-ready)
- **ML Model**: CLIP (OpenAI) via Hugging Face Transformers
- **Embeddings**: 768-dimensional vectors
- **Server**: Uvicorn (ASGI)

### Frontend
- **Framework**: React 19 (latest)
- **Language**: TypeScript (type-safe)
- **Bundler**: Vite (fast dev server)
- **Styling**: CSS3 (variables, gradients, animations)
- **Design**: Responsive, dark mode, professional UI

## 🔧 Configuration

### Environment Variables

**Backend** (`backend/.env`):
```bash
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/imagesearch
```

**Frontend** (`frontend/.env`):
```bash
VITE_API_URL=http://localhost:8000
```

## 📊 Model Performance

- **Model**: OpenAI CLIP ViT-B/32
- **Embedding Dim**: 768
- **Inference Time**: ~200ms per image
- **Memory**: 350MB model weights
- **Devices**: CPU (slow), GPU (fast)

## 🚦 Development

### Frontend Dev
```bash
cd frontend
npm run dev      # Start dev server with hot reload
npm run build    # Build for production  
npm run lint     # Run ESLint
npm run preview  # Preview production build
```

### Backend Dev
```bash
cd backend
pip install -e .  # Install in development mode
uvicorn app.main:app --reload  # Auto-reload on changes
```

### Database Migrations
Tables are auto-created on startup via SQLAlchemy. To reset:
```python
from app.database import Base, engine
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)
```

## 🧪 Testing

Upload test images and verify:
1. Images appear in `/static/images/`
2. Search returns similar results
3. Images appear in history view
4. Stats show correct count

## 📦 Deployment

### Docker (Recommended)
```bash
cd backend
docker compose up --build -d
cd ../frontend
docker build -t imagesearch-frontend .
docker run -p 3000:3000 imagesearch-frontend
```

### Cloud Platforms
- **Backend**: Heroku, AWS ECS, Google Cloud Run
- **Database**: AWS RDS, Heroku Postgres, Google Cloud SQL
- **Frontend**: Vercel, Netlify, AWS S3 + CloudFront

## 🐛 Troubleshooting

**Backend won't start**
```bash
# Check database connection
psql postgresql://postgres:postgres@localhost:5432/imagesearch
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

**Frontend build fails**
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run build
```

**CLIP model download slow**
- Model caches in `~/.cache/huggingface/`
- First run downloads 350MB
- Subsequent requests use cached version

**Search returns no results**
- Upload more images first
- Check database has images: `SELECT COUNT(*) FROM images;`

## 📚 Resources

- [CLIP Paper](https://arxiv.org/abs/2103.14030)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)

## 📜 License

MIT License - Feel free to use and modify!

## 👨‍💻 Author

Built with ❤️ for AI-powered image search.

---

**Status**: ✅ Production Ready | **Last Updated**: March 2026
