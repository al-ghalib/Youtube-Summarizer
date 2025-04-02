# 📺 YouTube Video Summarizer

## 🔥 Overview

YouTube Video Summarizer is a **Streamlit-based web app** that extracts transcripts from YouTube videos and generates concise summaries using **Google Gemini AI**. The app supports multiple summary types and allows downloading the output in **PDF** and **Markdown** formats.

## 🚀 Features

- 🎥 **Extract Transcripts**: Fetches YouTube video transcripts automatically.
- 🧠 **AI-Powered Summaries**: Generates summaries using Google Gemini AI.
- 📄 **Multiple Summary Types**: Choose between Short, Medium, and Detailed summaries.
- 📥 **Download Options**: Save summaries as **PDF** and **Markdown** files.
- ⚡ **Fast & Simple**: Streamlit-based UI for quick summarization.

## 🛠️ Installation

### 1️⃣ Clone the repository

```sh
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
```

### 2️⃣ Create a virtual environment (Optional but recommended)

```sh
python -m venv venv  # Windows: python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Set up API keys

Create a `.env` file in the project root and add your **Google API Key**:

```
GOOGLE_API_KEY=your_google_api_key_here
```

## ▶️ Usage

Run the Streamlit app:

```sh
streamlit run app.py
```

Then, open the local URL provided by Streamlit in your browser.

## 📌 How It Works

1. Enter the **YouTube Video URL**.
2. Choose the **summary type** (Short, Medium, Detailed).
3. Click **"Get Summary"**.
4. View and download the summary as a **PDF** or **Markdown**.

## 🛠️ Tech Stack

- **Python** 🐍
- **Streamlit** 🚀
- **Google Gemini AI** 🧠
- **YouTube Transcript API** 📜
- **FPDF** (for PDF generation) 📄

## 🤖 Future Improvements

- 🔄 Support for multilingual transcripts.
- 🎨 Improved UI design.
- 📊 Analytics on summary performance.
- 🔧 Fine-tuning the AI model for better accuracy.

## 📜 License

This project is licensed under the **MIT License**.

## 🙌 Contributing

Feel free to submit issues and pull requests!

## ⭐ Support

If you like this project, please consider giving it a **⭐ on GitHub!**

---

🚀 Happy Summarizing!
