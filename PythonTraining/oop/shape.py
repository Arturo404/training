from abc import ABC, abstractmethod 

class Shape(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def area(self):
        pass
        
    def __str__(self):
        return f"Color: {self._color}"