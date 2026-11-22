from flask import Flask, request, jsonify, send_file
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__, static_folder='.', static_url_path='')

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

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
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Sorry, I had an error: {str(e)}"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
