Personalized AI Quiz Master & Summarizer 🧠✨
An interactive, AI-powered web application designed to facilitate dynamic learning through conversational quizzing and instant, structured text summarization. Built using Python, Flask, HTML/JavaScript, and the Gemini API. 
📂 Project Structure
Plaintext
chatbot/
│
├── .env                  # Environment configuration & API keys
├── app.py                # Main Flask backend application server
├── requirements.txt      # Python package dependencies
└── templates/
    └── index.html        # Frontend user interface

🌟 Key Features
•	Interactive AI Quiz Buddy: Engages users in real-time, conversational quizzes on any study topic, testing conceptual understanding and providing immediate, constructive feedback. 
•	Chapter & Notes Summarizer: Instantly processes lengthy academic texts, articles, or notes and distills them into clean, structured bullet points highlighting core concepts. 
•	Responsive Web Interface: Features a dual-panel layout supporting simultaneous quiz sessions and text summarization.
🚀 Getting Started
Prerequisites
•	Python 3.8 or higher
•	A valid Google Gemini API Key
Installation & Setup
1.	Clone the repository:
Bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name/chatbot
2.	Install dependencies:
Bash
pip install -r requirements.txt
3.	Configure Environment Variables:
Create a .env file inside the chatbot/ directory and add your API key:
Code snippet
GEMINI_API_KEY=your_actual_api_key_here
4.	Run the Application:
Bash
python app.py
5.	Open your web browser and navigate to the local server address shown in your terminal (typically [http://127.0.0.1:5000](http://127.0.0.1:5000)).
💡 Usage Guide
1.	Quiz Buddy: Type your study topic or answer questions directly in the chat input on the left to test your knowledge interactively. 
2.	Notes Summarizer: Paste dense academic text or chapters into the right-hand input box and click Generate Structured Summary to view concise key takeaways. 

