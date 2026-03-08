←
←
# 导入shapes模块
import shapes
if __name__ == "__main__":
    RArea = shapes.rectangle_area(5, 3)
    RPerimeter = shapes.rectangle_perimeter(5, 3)
    SArea = shapes.square_area(4)
   
    print(str(RArea))
    print(str(RPerimeter))
    print(str(SArea))

from shapes import rectangle_area, rectangle_perimeter, square_area
if __name__ == "__main__":
    RArea2 = rectangle_area(5, 3)
    RPerimeter2 = rectangle_perimeter(5, 3)
    SArea2 = square_area(4)
    print(str(RArea2))
    print(str(RPerimeter2))
    print(str(SArea2))