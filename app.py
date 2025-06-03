from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/set-status', methods=['GET', 'POST'])
def mock_endpoint():
    return jsonify({"message": "Success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
