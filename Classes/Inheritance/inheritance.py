#inheritance means a child class can access the properties of a parent class

class Employee: 
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

class SoftwareEnginer(Employee):
    def __init__(self,name,age,level,salary):
        super().__init__(name,age,salary)
        self.level=level

    def debug(self):
        print(f"{self.name} is debugging...and age is {self.age}")    


class Designer(Employee):
    def __init__(self,name,age,level,salary):
        super().__init__(name,age,salary)
        self.level=level

    def design(self):
        print(f"{self.name} is designing....and age is {self.age}")    


s1=SoftwareEnginer("yashu",18,1,50000)
s2=Designer("Nandhu",19,2,60000)
print(s1.name)
print(s1.age)
print(s1.salary)
print(s1.level)
print(s2.name)
print(s2.age)
print(s2.salary)
print(s2.level)
s1.debug()
s2.design()