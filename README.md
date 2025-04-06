# Gemini Image Generation API (using shell script) 🎨✨

This project is a simple Python CLI tool that generates images using the Gemini API (Google's generative AI). It takes a text prompt and returns an AI-generated image, saved locally.

---

## 📁 Project Structure

```
gemini-image-generation-api/
├── .env                         # Contains your GEMINI_API_KEY
├── gemini-image-generation-exp.py  # Main Python script
├── requirements.txt             # Python dependencies
└── run.sh                       # Shell script to setup and run the project
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Ryan-PG/gemini-image-generation-api
cd gemini-image-generation-api
```

### 2. Create `.env` File

Create a `.env` file in the root with your API key:

```
GEMINI_API_KEY=your_google_api_key_here
```

> 💡 Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### 3. Run the Script

```bash
chmod +x run.sh
./run.sh
```

You'll be prompted to enter:
- A **text prompt** (e.g., `A futuristic city at night`)
- A **file name** for the image (e.g., `output_image`)

The image will be saved as `output_image.png`.

---

## 📦 Dependencies

Listed in `requirements.txt`:
- `python-dotenv`
- `google-generativeai`

---

## 🛡️ Notes

- Do **not commit** your `.env` file or `.venv` directory.
- Add this to your `.gitignore`:

```
.venv/
.env
__pycache__/
```

---

## 📸 Example Output

Prompt: `A cat wearing sunglasses on the beach`  
Output: `cat_beach.png`

![Example Image](./image.png)

---

## 🛠️ License

MIT License © 2025 [Your Name]
