import os
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI


load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def process_image(img):
    print("Processing the image...")
    ext = Path(img.name).suffix.lower()
    file_bytes = img.read()

    if ext in ['.jpg', '.jpeg', '.png']:
        print(f"Image format: {ext}")
        response = client.chat.completions.create(
            model="gpt-4.1-mini")