# 📚 TutorMind – AI-Powered Study Assistant Suite

**TutorMind** is a modular Streamlit application built for students, educators, and researchers. It leverages powerful LLMs via Groq to offer automated note-taking, document summarization, resume evaluation, plagiarism detection, and much more — all in one dashboard.

---

## 🔧 Features

| Tool                         | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| 📝 Documents Summarizer     | Summarize academic PDFs into clean, exam-ready notes                        |
| 📚 Chat with Your PDFs      | Ask questions and get instant answers from uploaded PDF files               |
| 🔍 Resume Checker           | Evaluate resumes against job descriptions using ATS logic                   |
| 🌐 Website Summarizer       | Extract and summarize readable text from web pages                         |
| 🎥 YouTube Summarizer       | Pull transcripts from videos and turn them into structured notes            |
| 🧠 Plagiarism Checker       | Identify copied or repetitive content and get rewriting suggestions         |
| 🖼️ Image-to-Text Notes      | Extract handwritten/printed notes from images and convert them to summaries  |

---

## 🚀 Technologies Used

- **Frontend**: Streamlit  
- **LLM Engine**: Groq API (LLaMA 3, Compound Beta)  
- **Embeddings**: HuggingFace or OpenAI  
- **OCR**: Tesseract via `pytesseract`  
- **PDF/Text Extraction**: `PyPDF2`, `langchain_community`  
- **Vector DB**: FAISS  
- **Summarization**: LangChain `map_reduce` chains

---

## ⚙️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/rohitkrishnanm/tutormind.git
cd tutormind
```

2. **Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Add your API keys**  
Create a `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_groq_key_here"
OPENAI_API_KEY = "optional_openai_key_here"
```

5. **Run the app**
```bash
streamlit run TutorMind.py
```

---

## 📁 Project Structure

```
TutorMind/
│
├── TutorMind.py                 # Main interface
├── text_summarizer/app11.py
├── chat_with_pdf/chat_with_pdf.py
├── Resume_ATS_tracker/resume_analyser.py
├── website_text_summarizer/app.py
├── youtube_video_summarizer/app.py
├── plagiarism_checker/app.py
├── image_to_text_notes/app.py
└── .streamlit/secrets.toml     # API keys
```

---

## ✍️ Author

**Rohit Krishnan**  
Business and Technology Strategist  
📧 rohitkrishnanm@gmail.com  
🌐 [rohitkrishnan.co.in](https://rohitkrishnan.co.in)  
🔗 [LinkedIn](https://linkedin.com/in/rohit-krishnan-320a5375) | [GitHub](https://github.com/rohitkrishnanm)

---

## ⚖️ License

© 2025 Rohit Krishnan. All rights reserved.  
This project is proprietary and cannot be reproduced or redistributed without explicit permission.