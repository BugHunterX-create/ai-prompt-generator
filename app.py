from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# Securely fetch the API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET"])
def home():
    return "Flask app is running!"

@app.route("/generate-prompt", methods=["POST"])
def generate_prompt():
    data = request.json
    topic = data.get("topic", "")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate an optimized AI prompt for: {topic}",
        max_tokens=100
    )

    return jsonify({"generated_prompt": response.choices[0].text.strip()})

if __name__ == "__main__":
    print("Flask is running on port 5000")
    app.run(host="0.0.0.0", port=5000)
