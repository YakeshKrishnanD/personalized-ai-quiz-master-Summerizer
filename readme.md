# Personalized AI Quiz Master & Summarizer 🧠✨

An interactive, AI-powered web application designed to facilitate dynamic learning through conversational quizzing and instant, structured text summarization.

## ✨ Features

* 🧠 **Interactive AI Quiz Buddy** — Engages users in real-time, conversational quizzes on any study topic, testing conceptual understanding and providing immediate, constructive feedback.
* 📄 **Chapter & Notes Summarizer** — Instantly processes lengthy academic texts, articles, or notes and distills them into clean, structured bullet points highlighting core concepts.
* 💻 **Responsive Web Interface** — Features a clean, modern dual-panel layout supporting simultaneous quiz sessions and text summarization.

## 📸 Screenshots

### 🖥️ Application Dashboard & Dual-Panel View

![Application Interface](screenshots/Screenshot%202026-10-13%20122306.png)

![Quiz & Summarizer View](screenshots/Screenshot%202026-10-13%20122526.png)

## 🛠️ Tech Stack

### Frontend & UI

HTML • JavaScript • CSS • Responsive Layout

### Backend

Python • Flask

### AI & Processing

Google Gemini API

## 🏗️ Architecture

```text
                 ┌─────────────────────┐
                 │    Web Interface    │
                 │   HTML / JavaScript │
                 └──────────┬──────────┘
                            │
                      HTTP Request
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Flask Server     │
                 │     Python Backend  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │  Google Gemini API  │
                 └─────────────────────┘

```

## ⚙️ Requirements

Before running the application, make sure you have installed:

* Python 3.8 or higher
* Git
* Google Gemini API Key

## 🚀 Installation

### 1. Clone the repository

```bash
git clone [https://github.com/YakeshKrishnanD/personalized-ai-quiz-master-Summerizer.git](https://github.com/YakeshKrishnanD/personalized-ai-quiz-master-Summerizer.git)
cd personalized-ai-quiz-master-Summerizer/chatbot

```

### 2. Install dependencies

```bash
pip install -r requirements.txt

```

### 3. Backend & Environment Setup

Create a `.env` file inside the `chatbot/` directory:

```env
GEMINI_API_KEY=your_actual_api_key_here

```

### 4. Run the Application

```bash
python app.py

```

Open your web browser and navigate to the local server address:

`http://127.0.0.1:5000`

## 🔑 Environment Variables

Keep all private configuration values secure in your `.env` file.

Never commit:

* Google Gemini API keys

## 💡 How to Use

1. **Quiz Buddy Panel (Left):** Type your study topic or answer questions directly in the chat input box to test your knowledge interactively.
2. **Notes Summarizer Panel (Right):** Paste dense academic text or chapters into the right-hand input box and click **Generate Structured Summary** to view concise key takeaways.

## 📌 Future Improvements

* User authentication and saved quiz history
* Multi-format document uploads (PDF, DOCX)
* Automated flashcard generation from notes
* Performance analytics and study progress tracking
* Real-time collaboration features

## 👨‍💻 Author

**Yakesh Krishnan D**

*Personalized AI Quiz Master & Summarizer — AI-powered learning and summarization tool.*

⭐ If you find this project useful, consider giving the repository a star.
