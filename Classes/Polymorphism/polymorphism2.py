class Circle:

    def area(self,r):
        return(f"3.14 * {r} * {r}")

class square(Circle):
    def area(self,r):
        return(f"{r} * {r}")

class rectangle(Circle):
    def area(self,r):
        return(f"4 * {r}")   

c1=Circle()
print(c1.area(5)) 

s1=square()
print(s1.area(5)) 

r1=rectangle()
r1.area(5)             


