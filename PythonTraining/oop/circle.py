from shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius

    @property
    def diameter(self):
        return 2*self._radius

    @diameter.setter
    def diameter(self, new_diameter):
        self._radius = new_diameter/2
    
    def area(self):
        return pi*(self._radius**2)
    
    def __str__(self):
        return f"{super().__str__()}, Shape: Circle, radius: {self._radius}"
    
    def __add__(self, other):
        new_radius = self._radius + other._radius
        return Circle(self._color, new_radius)