from flask import Flask, request, jsonify
import openai
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests
CORS(app, origins=["https://timely-mochi-f742c7.netlify.app/"])
openai.api_key = os.getenv("OPENAI_API_KEY")
# Predefined context about Iron Lady
context = """
Iron Lady offers a 12-week online leadership program. It includes topics like leadership, communication, and career growth.
Participants get a certificate and are assigned a mentor. The program is fully online.
"""
@app.route('/')
def index():
    return "Iron Lady Chatbot API is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers FAQs about Iron Lady’s leadership program."},
            {"role": "user", "content": context},
            {"role": "user", "content": user_message}
        ]
    )
    reply = response.choices[0].message.content.strip()
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
