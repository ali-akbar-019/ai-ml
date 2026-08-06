from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def abs(self):
        pass

def Circle(Shape):
    def area(self):
        return 3.15 * 5 * 5