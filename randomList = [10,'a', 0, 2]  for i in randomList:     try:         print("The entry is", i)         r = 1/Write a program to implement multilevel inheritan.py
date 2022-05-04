class Stud:
    def __init__(self,rn,name):
        self.rn=rn
        self.name=name
class Marks(Stud):
    def __init__(self, rn,name,m1,m2):
        Stud.__init__(self, rn, name)
        self.m1=m1
        self.m2=m2
    def calc(self):
        self.tot=self.m1+self.m2
        self.per=(self.tot*100)/200
class Result(Marks):
    def __init__(self,rn,name,m1,m2):
        Marks.__init__(self, rn, name,m1, m2)
    def disp(self):
        self.calc()
        if self.m1<40 or self.m2<40:
            print(self.name,"Result:Fail")
        elif self.per<60:
            print(self.name,"Pass with Grade B")
        elif self.per < 70:
            print(self.name,"Pass with Grade A")
        else:
            print(self.name,"Pass with Grade O")
s1=Result(1,"Sam",78,90)
s2=Result(1,"Ram",28,40)

s1.disp()
s2.disp()
input()
