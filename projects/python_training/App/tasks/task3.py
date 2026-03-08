←
←
from flask import Flask, request, jsonify
from datetime import datetime
app = Flask(__name__)

@app.route('/api/time', methods = ['GET'])
def current_time():
    current_time = datetime.now().isoformat()
    return jsonify({
        "current_time": current_time
    })
if __name__ == "__main__":
    app.run(port=8000)
