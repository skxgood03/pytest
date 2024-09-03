from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Hello, World!")


@app.route('/greet/<name>')
def greet(name):
    return jsonify(message=f"Hello, {name}!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
