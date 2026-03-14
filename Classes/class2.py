class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        return f"name={self.name} and age={self.age}" 


    def __sub__(self,other):
        return  self.age-other.age

    def __add__(self,other):
         return  self.age + other.age


    def __mul__(self,other):
        return self.age*other.age   

    def __truediv__(self,other):
        return self.age/other.age   



s1=Student("yashu",18)
s2=Student("Nandhu",19)
print(s1-s2)
print(s1+s2)
print(s1*s2)
print(s1/s2)
print(s1.info())            







