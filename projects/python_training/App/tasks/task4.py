←
←
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/api/echo", methods=['POST'])
def echo():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    data["received"] = True
    return jsonify(data), 200
if __name__ == "__main__":
    app.run(port=8000)