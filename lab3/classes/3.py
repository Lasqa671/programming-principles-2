"""
Define a class named Rectangle which inherits 
from Shape class from task 2. Class instance 
can be constructed by a length and width. 
The Rectangle class has a method which can 
compute the area.
"""
class shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class rectangle(shape):
    def __init__(self, length, width):
     super().__init__()
     self.length = length
     self.width = width
    def area(self):
       return self.length * self.width

rect = rectangle(7, 3)
print(rect.area())