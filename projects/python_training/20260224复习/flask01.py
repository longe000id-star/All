←
←
from flask import Flask

app = Flask(__name__)

@app.get("/")
def add():
    a = 20000
    b = 10000
    add = a + b
    return str(add)

if __name__ == "__main__":
    print("goto: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
    