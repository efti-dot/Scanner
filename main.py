import os
import numpy as np
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def process_image(img):
    print("Processing the image...")
    ext = Path(img.name).suffix.lower()
    file_bytes = img.read()