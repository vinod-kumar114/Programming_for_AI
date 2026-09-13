# Abstraction is the process of hiding unnecessary implementation details and showing only the essential features of an object.

# It allows programmers to focus on what an object does rather than how it does it. 

# In Python, abstraction can be implemented using abstract classes and abstract methods from the abc module.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side=side

    def area(self):
        return self.side**2

circle = Circle(12)
square = Square(4)

print("The area of the circle is ",circle.area())
print("The area of the square is ",square.area())