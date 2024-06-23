from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    response = generate_response(user_message)
    return jsonify({"response": response})

def generate_response(user_message):
    try:
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=f"User: {user_message}\nBot:",
            max_tokens=150,
            n=1,
            stop=["\n"],
            temperature=0.7,
        )
        bot_message = response.choices[0].text.strip()
        return bot_message
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
