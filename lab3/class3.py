class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
shape = Shape()
print("Area of generic shape:", shape.area()) 

square = Square(4)
print("Area of square with length 4:", square.area()) 

rectangle = Rectangle(5,6)
print("Area of rectangle with length 5 and width 6:", rectangle.area()) 
