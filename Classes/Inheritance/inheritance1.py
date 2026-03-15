#Example 2
class Animal:
    def __init__(self, speciman):
        self.speciman = speciman

    def eat(self):
        print(f"{self.speciman} Eats Food..")

class Dog(Animal):
    def __init__(self, speciman):
        super().__init__(speciman)

    def dog(self, food):
        print(f"Dog Eats {food}")

    def bark(self):
        print("Dog Barks")

class Cat(Animal):
    def __init__(self, speciman):
        super().__init__(speciman)

    def cat(self, food):
        print(f"Cat Eats {food}")   

    def meow(self):
        print("Cat Meows")        

d1=Dog("Breed")
d1.eat()
d1.bark()
d1.dog("Chicken")

c1=Cat("Feline")
c1.eat()
c1.meow()
c1.cat("Rat")
