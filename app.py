from flask import Flask, request, jsonify
from guesslang import Guess

app = Flask(__name__)
guess = Guess()

@app.route('/detect', methods=['POST'])
def detect_language():
    text = request.data.decode('utf-8')
    language = guess.language_name(text)
    return jsonify({'language': language})

@app.route('/')
def hello_world():
    return 'Hello World from Guesslang server!'

if __name__ == '__main__':
    app.run(debug=True)
    # To test the /detect endpoint, you can use the following curl command:
    # curl -X POST -H "Content-Type: application/json" -d '{"text": "print(\"Hello, World!\")"}' http://127.0.0.1:5000/detect