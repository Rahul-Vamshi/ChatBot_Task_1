from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app, origins=["https://timely-mochi-f742c7.netlify.app"])

# Initialize OpenAI client (picks up API key from environment variable)
client = OpenAI()

@app.route('/')
def home():
    return "Iron Lady Chatbot API is running!"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '')
        print(f"Received: {user_message}")

        if not user_message:
            return jsonify({"reply": "Please enter a message."}), 400

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers FAQs about Iron Lady’s leadership programs."},
                {"role": "user", "content": user_message}
            ]
        )

        reply = response.choices[0].message.content.strip()
        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Sorry, something went wrong on the server."}), 500
