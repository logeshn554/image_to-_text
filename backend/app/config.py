import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

# CORS Origins - allow common development ports
CORS_ORIGINS = os.getenv(
    "CORS_ORIGINS", 
    "http://localhost:3000,http://localhost:5173,http://localhost:5174,http://localhost:5175,http://localhost:5176"
).split(",")

# Model settings
MODEL_NAME = os.getenv("MODEL_NAME", "Salesforce/blip-image-captioning-base")
MAX_IMAGE_SIZE_MB = int(os.getenv("MAX_IMAGE_SIZE_MB", "10"))
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "gif", "webp"}

DESCRIPTION = "AI Image Caption Generator - Generate text descriptions from images using BLIP"
VERSION = "1.0.0"



