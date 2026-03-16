from io import BytesIO
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

_model = None
_processor = None


def _load_model():
    global _model, _processor
    if _model is None:
        _processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        _model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return _model, _processor


def generate_caption_from_bytes(data: bytes) -> str:
    """Generate text caption from image bytes using BLIP."""
    model, processor = _load_model()
    image = Image.open(BytesIO(data)).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    
    with torch.no_grad():
        out = model.generate(**inputs, max_length=50)
    
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption


def generate_caption_from_path(path: str) -> str:
    """Generate text caption from image file path using BLIP."""
    with open(path, "rb") as f:
        return generate_caption_from_bytes(f.read())

