import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print("Coordinates of the point: ({}, {})".format(self.x, self.y))
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance
point1 = Point(3, 4)
point2 = Point(6, 8)

point1.show()
point2.show() 

point1.move(1, -2)
point1.show() 

distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)
    