from abc import ABC, abstractmethod

''' 
    An interface in python refers to an abstract base class (ABC) in which 
    all methods are abstract in nature.
'''

class Shape(ABC):

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def display(self):
        print("Square with sides:", self.side)

    def area(self):
        print("Square Area:", self.side * self.side)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def display(self):
        print(f"Circle with radius: {self.radius}")

    def area(self):
        import math
        print("Circle Area:", math.pi * (self.radius ** 2))


square = Square(4)
square.display()  # Output: Square with side: 4
square.area()  # Output: 16
#
circle = Circle(3)
circle.display()  # Output: Circle with radius: 3
circle.area()  # Output: 28.274333882308138