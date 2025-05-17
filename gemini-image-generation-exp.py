import os
import mimetypes
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def save_binary_file(file_name, data):
    with open(file_name, "wb") as f:
        f.write(data)

def generate(text: str = "Hello", file_name: str = "image.png"):
    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

    model = genai.GenerativeModel("gemini-2.0-flash-preview-image-generation")

    chat = model.start_chat()

    stream = model.generate_content(
        text,
        stream=True,
        generation_config={
            "response_mime_type": "text/plain",  # You can change this to "image/jpeg" etc.
        }
    )

    for chunk in stream:
        parts = chunk.parts
        if parts and hasattr(parts[0], "inline_data"):
            inline_data = parts[0].inline_data
            mime_type = inline_data.mime_type
            file_extension = mimetypes.guess_extension(mime_type)
            file_path = f"{file_name}{file_extension}"
            save_binary_file(file_path, inline_data.data)
            print(f"✅ File saved to: {file_path}")
        elif chunk.text:
            print("Text output:", chunk.text)

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate an image from text using Gemini.")
    parser.add_argument("--text", required=True, help="Prompt text to generate the image")
    parser.add_argument("--file_name", default="image", help="Base name for the output image file")

    args = parser.parse_args()
    generate(text=args.text, file_name=args.file_name)
