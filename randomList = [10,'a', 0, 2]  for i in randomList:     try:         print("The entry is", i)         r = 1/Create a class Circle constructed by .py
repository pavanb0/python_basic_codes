class Circle:
    pi=3.14
    def __init__(self, r):
        self.radius = r     
    def area(self):
        return self.radius**2*Circle.pi
    def perimeter(self):
        return 2*self.radius*Circle.pi

c=[]
for i in range(3):
    r=int(input("Enter radius"))
    c.append(Circle(r))
for i in c:
    print("Area of Circle:",i.area())
    print("Perimeter of Circle:",i.perimeter())

input()
