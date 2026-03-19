class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def topper(self):
        pass

    def Fail(self):
        pass

class Topper_Student(Student):
    def __init__(self,name,age,marks):
        super().__init__(name,age,marks) 

    def topper(self):
       if self.marks > 80:
        print(f" {self.name} is Topper with the marks of {self.marks}/100 ")


    def Fail(self):
        if self.marks < 40 and self.marks > 35:
            print(f"Border pass {self.marks}")   

t=Topper_Student("Yashu",18,98)
t.topper()
t.Fail()


