import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv  # <-- ADDED: To load environment variables from .env
from google import genai
from google.genai import types

# Load environment variables from the .env file cleanly at runtime
load_dotenv()

app = Flask(__name__)

# Fetch the API key automatically from your system environment / .env file
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("System Error: GEMINI_API_KEY is missing from your .env file!")

client = genai.Client(api_key=API_KEY)

# Using the fast, free-tier flash model
MODEL_ID = 'gemini-2.5-flash'

# System instructions to set up the AI Study Buddy persona
STUDY_BUDDY_PROMPT = """
You are an expert AI Study Buddy. Your job is to quiz the user on a topic of their choice. 
Ask exactly ONE conceptual question at a time. Wait for their answer.
When they answer, evaluate if they are correct, explain why/why not briefly, and ask the next question.
Keep your responses encouraging, concispye, and formatted nicely in Markdown.
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_data = request.json
    user_message = user_data.get("msg", "")
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=user_message,
            config=types.GenerateContentConfig(
                system_instruction=STUDY_BUDDY_PROMPT,
                temperature=0.7
            )
        )
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"response": f"Backend Error: {str(e)}"})

@app.route("/summarize", methods=["POST"])
def summarize():
    user_data = request.json
    raw_text = user_data.get("text", "")
    
    if len(raw_text.strip()) < 50:
        return jsonify({"summary": "Please provide a longer piece of text (at least 50 characters) to summarize."})
        
    try:
        summary_prompt = f"Provide a concise summary of the following academic text. Use bullet points for key concepts and bold important terms:\n\n{raw_text}"
        
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=summary_prompt
        )
        return jsonify({"summary": response.text})
    except Exception as e:
        return jsonify({"summary": f"Backend Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)