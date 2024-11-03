from flask import Flask, request, jsonify
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the API!", "status": "success"}), 200

@app.route('/api/data', methods=['GET'])
def get_data():
    time.sleep(3)
    return jsonify({"message": "Hello, World!", "status": "success"}), 200

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.json
    time.sleep(3)
    return jsonify({"received": data, "status": "success"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
