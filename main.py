import os
import base64
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def process_image(img):
    ext = Path(img.name).suffix.lower()
    file_bytes = img.read()

    if ext in ['.jpg', '.jpeg', '.png']:
        # Convert bytes to base64 string
        b64_image = base64.b64encode(file_bytes).decode("utf-8")

        response = client.chat.completions.create( 
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI that extracts product details from images. "
                        "Always return valid JSON with keys: title, color, size, brand, description, quantity. "
                        "The 'quantity' must be a number only (e.g., 1, 2, 3)."
                    )
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Analyze this image and return product details including numeric quantity."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/{ext[1:]};base64,{b64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=300
        )

        return response.choices[0].message.content
    else:
        return "Unsupported file format."