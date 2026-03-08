←
←
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/test', methods=['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE'])
def test():
    print(f"request method: {request.method}")
    print(f"request headers: {dict(request.headers)}")
    return jsonify({
        "method": request.method,
        "message": "Test endpoint working"
    })
app.run(port=8000)