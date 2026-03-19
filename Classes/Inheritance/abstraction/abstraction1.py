# Abstraction means hiding the internal implementation details and showing only the essential features of an object.

class SoftwareEngineer:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self._salary=salary

    def __abstractmethod__(self):
        pass

    def work(self):
        pass

    def get_salary(self):
        pass

class FrontendEngineer(SoftwareEngineer):
    def __init__(self,name,age,_salary):
        super().__init__(name,age,_salary)

    def work(self):
        print(f"{self.name} is working on the frontend")

    def get_salary(self):
        print(f"Frontend Engineer get salary around {self._salary}")    

class BackendEngineer(SoftwareEngineer):
    def __init__(self,name,age,_salary):
        super().__init__(name,age,_salary)

    def work(self):
        print(f"{self.name} is working on the backend")

    def get_salary(self):
        print(f"Backend Engineer get salary around {self._salary}")    
    

class FullstackEngineer(FrontendEngineer,BackendEngineer):
    def __init__(self,name,age,_salary):
        super().__init__(name,age,_salary)

    def work(self):
        print(f"{self.name} is working on the frontend and backend")

    def get_salary(self):
        print(f"Full stacker Engineer get salary around {self._salary}")    
    


fe=FrontendEngineer("John",25,5000)
be=BackendEngineer("Doe",26,10000)
ff=FullstackEngineer("yashu",18,20000)
ff.get_salary()
fe.get_salary()
be.get_salary()
ff.work()
fe.work()
be.work()        

    