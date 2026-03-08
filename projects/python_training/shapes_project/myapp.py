←
←
from flask import Flask
import shapes

myapp = Flask(__name__)

@myapp.get("/area/<int:length>/<int:width>")
def area(length, width):
    area = shapes.rectangle_area(length, width)
    return f"长方形的面积是：{area}"
@myapp.get("/perimeter/<int:length>/<int:width>")
def perimeter(length, width):
    perimeter = shapes.rectangle_perimeter(length, width)
    return str(perimeter)

if __name__ == "__main__":
    myapp.run()