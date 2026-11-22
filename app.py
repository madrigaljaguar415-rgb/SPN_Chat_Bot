from flask import Flask, request, jsonify, send_file
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3.5-flash")

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    # SPN Personality
    prompt = f"You are SPN, a friendly, smart AI assistant. Answer helpfully and in a simple, friendly way. User says: {user_message}"
    
    try:
        response = model.generate_content(prompt)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Sorry, I had an error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)