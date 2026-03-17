class Circle:

    def area(self,r):
        print(f"3.14 * {r} * {r}")

class square(Circle):
    def area(self,r):
        print(f"{r} * {r}")

class rectangle(Circle):
    def area(self,r):
        print(f"4 * {r}")   

c1=Circle()
c1.area(5) 

s1=square()
s1.area(5) 

r1=rectangle()
r1.area(5)             


