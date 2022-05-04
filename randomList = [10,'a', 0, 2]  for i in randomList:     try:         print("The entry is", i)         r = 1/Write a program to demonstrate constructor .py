class Emp:
    empcount=0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Emp.empcount+=1
    def dispEmp(self):
      print ("Name : ", self.name,  "\nSalary: ", self.salary)
    def __del__(self):
        print("Object Removed")
        Emp.empcount-=1
emp1 = Emp("Sam", 72000)
emp2 = Emp("Ram", 40000)
emp1.dispEmp()
emp2.dispEmp()
print("Total Number of Employee:",Emp.empcount)
del emp1
print("Total Number of Employee:",Emp.empcount)

input()
