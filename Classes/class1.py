
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"name={self.name} and age={self.age}"

    def __add__(self,other):
        return self.age+other.age
    

    def __eq__(self,other):
        if self.name==other.name and self.age==other.age:
            return True
        else:
            return False


s1=Student("yashu",18)
s2=Student("Nandhu",19)
s3=Student("yashu",18)
print(s1.age)
print(s1.name)
print(s2.name)
print(s2.age)
print(s2==s3)





    