from abc import ABC,abstractmethod
class Shape(ABC):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @abstractmethod
    def area(self):
        pass
class Rect(Shape):
    def __init__(self,x,y):
        Shape.__init__(self,x,y)
    def area(self):
        return(self.x*self.y)
class Tri(Shape):
    def __init__(self, x, y):
        Shape.__init__(self, x, y)

    def area(self):
        return (self.x * self.y)/2
r=Rect(2,3)
t=Tri(5,6)
print("Area of Rect:",r.area())
print("Area of Tri:",t.area())
