class Data:
    def __init__(self,n):
        self.n=n
    def  __gt__(self, other):
        if self.n > other.n:
            return True
        else:
            return False
    def __add__(self, other):
        return(self.n+other.n)

d1=Data(10)
d2=Data(3)
print("Addition of two objects:",d1+d2)
print("Largest from two objects:")
if d1 > d2:
    print(d1.n,"is greater")
else:
    print(d2.n," is greater")
input()
