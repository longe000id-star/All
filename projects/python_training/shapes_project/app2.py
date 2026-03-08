←
←
import shapes2
from flask import Flask

app2 = Flask(__name__)

@app2.get("/circle_area/<int:radius>")
def circle_area(radius):
    circle_area = shapes2.circle_area(radius)
    return circle_area

if __name__  == "__main__":
    app2.run()

