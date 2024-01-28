from shape import Shape

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self._width = width
        self._height = height

    def area(self):
        return self._width*self._height
    
    def __str__(self):
        return f"{super().__str__()}, Shape: Rectangle, dimensions: {self._width}x{self._height}"
    
    def __add__(self, other):
        new_width = self._width + other._width
        new_heigth = self._height + other._height
        return Rectangle(self._color, new_width, new_heigth)
    

    def __lt__(self, other):
        return self.area() < other.area()
    
    def __gt__(self, other):
        return self.area() > other.area()