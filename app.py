from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app and enable CORS for your frontend domain
app = Flask(__name__)
CORS(app, origins=["https://timely-mochi-f742c7.netlify.app"])

# 🔒 Hardcoded FAQ data
faq_data = {
    "what is the duration of the program?": "The Iron Lady leadership program lasts for 12 weeks.",
    "is the program online or offline?": "The program is conducted fully online with live interactive sessions.",
    "do i get a certificate?": "Yes, you will receive a certificate of completion at the end of the program.",
    "who are the mentors?": "Our mentors are experienced women leaders from various industries who guide and support you through the program.",
    "what is the cost of the program?": "The program fee is shared during the application process based on eligibility and scholarships.",
    "how do i apply?": "You can apply through our official website by filling out the application form.",
    "are there any scholarships?": "Yes, scholarships are available based on merit and need."
}

@app.route('/')
def home():
    return "Iron Lady Chatbot API is running with hardcoded FAQs!"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get('message', '').strip().lower()
        print(f"Received: {user_message}")

        if not user_message:
            return jsonify({"reply": "Please enter a question."}), 400

        # Match user question
        reply = faq_data.get(user_message, "Sorry, I don’t know the answer to that. Please check our website or contact support.")

        return jsonify({"reply": reply})

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Something went wrong on the server."}), 500

# Run the app (only locally — not used on Render)
if __name__ == '__main__':
    app.run(debug=True)
