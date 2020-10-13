# abstract method and abstract base class
# abstract method is used when we want some function to apply over all the subclasses


# from abc import ABCMeta, abstractmethod

# if we are using 3.4+ python
from abc import ABC, abstractmethod


# class Shape(metaclass=ABCMeta):
class Shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def print_area(self):
        return self.length * self.breadth


rect = Rectangle()
print(rect.print_area())

# we cant make objects of abstract base class
# s=Shape()
# The base class of the class hierarchy.
# When called, it accepts no arguments and returns a new featureless instance that has no instance attributes and cannot be given any.
