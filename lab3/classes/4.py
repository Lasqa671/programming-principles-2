"""
Write the definition of a Point class. Objects from this class should have a

a method show to display the coordinates of the point
a method move to change these coordinates
a method dist that computes the distance between 2 points
"""
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
point1 = Point(3, 4)
point2 = Point(5, 6)

point1.show()  

point1.move(7, 8)
point1.show()  

distance = point1.dist(point2)
print(distance)  