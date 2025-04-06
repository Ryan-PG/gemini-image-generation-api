# Gemini Image Generation API (using shell script) 🎨✨

This project is a Python-based CLI tool that generates images using the **Gemini API** (Google's generative AI). It uses a **text prompt** to create an AI-generated image and saves it locally. A shell script automates environment setup and script execution.

---

## 📁 Project Structure

```
gemini-image-generation-api/
├── .env                            # Contains your GEMINI_API_KEY
├── generate_image.py               # Main Python script
├── requirements.txt                # Python dependencies
├── run.sh                          # Shell script to setup and run the project
└── README.md                       # Project documentation
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Ryan-PG/gemini-image-generation-api
cd gemini-image-generation-api
```

### 2. Create `.env` File

Create a `.env` file in the root of the project:

```
GEMINI_API_KEY=your_google_api_key_here
```

> 💡 You can get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

---

## 🖼️ Usage

### Step-by-Step (via Shell Script)

1. Make the script executable:

```bash
chmod +x run.sh
```

2. Run the project with a **prompt** and **file name**:

```bash
./run.sh "A futuristic city at sunset" sunset_city
```

This will:
- Use `"A futuristic city at sunset"` as the generation prompt
- Save the result as `sunset_city.png` (or with another appropriate extension depending on MIME type)

---

## 🧪 Example

```bash
./run.sh "A cat wearing sunglasses on the beach" cat_beach
```

**Output:** `cat_beach.png`

![Example Image](./image.png)

---

## 🧰 Python Script CLI Usage (Alternative)

You can run the Python script directly:

```bash
python generate_image.py --text "A robot cooking breakfast" --file_name robot_breakfast
```

---

## 📦 Dependencies

Install via `requirements.txt`:

- `python-dotenv`
- `google-generativeai`

> These will be installed automatically when you run `run.sh`.

---

## 🛡️ Best Practices

- Do **not commit** your `.env` file or `.venv` folder.
- Add these lines to your `.gitignore`:

```
.venv/
.env
__pycache__/
```

---

## 📄 License

MIT License © 2025 [Your Name]
