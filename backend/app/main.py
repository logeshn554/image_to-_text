import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .config import CORS_ORIGINS, DESCRIPTION, VERSION
from .embeddings import generate_caption_from_bytes
from .utils import is_valid_image_file

# Create app
app = FastAPI(
    title="Image Caption Generator API",
    description=DESCRIPTION,
    version=VERSION,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "version": VERSION, "model": "BLIP"}


@app.post("/generate-caption")
async def generate_caption(file: UploadFile = File(...)):
    """Generate a text caption from an image."""
    if not is_valid_image_file(file.filename or ""):
        raise HTTPException(status_code=400, detail="Invalid file type. Allowed: jpg, png, gif, webp")
    
    contents = await file.read()
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="File is empty")

    try:
        caption = generate_caption_from_bytes(contents)
        return {
            "caption": caption,
            "message": "Caption generated successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Caption generation failed: {str(e)}")

        db.close()

    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "images": [{"id": img.id, "filename": img.filename, "caption": img.description} for img in images]
    }


@app.delete("/image/{image_id}")
async def delete_image(image_id: int):
    """Delete an image."""
    db = SessionLocal()
    try:
        img = db.query(models.Image).filter(models.Image.id == image_id).first()
        if not img:
            raise HTTPException(status_code=404, detail="Image not found")
        
        # Delete file
        try:
            os.remove(os.path.join(str(STATIC_DIR), img.filename))
        except:
            pass
        
        db.delete(img)
        db.commit()
        return {"message": "Image deleted"}
    finally:
        db.close()

