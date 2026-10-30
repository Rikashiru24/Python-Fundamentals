
# Parent or Base Class
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Child or Subclass
class Mammal(Animal):
    def walk(self):
        print("walk")


# Child or Subclass
class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
