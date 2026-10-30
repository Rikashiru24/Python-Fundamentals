# object = is the base class of all the python's classes. Directly or Indirectly derived from the object class


# Parent or Base Class
class Animal:  # behind the scene Animal(object)
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Child or Subclass
class Mammal(Animal):  # behind the scene Mammal(object)
    def walk(self):
        print("walk")


# Child or Subclass
class Fish(Animal):  # behind the scene Fish(object)
    def swim(self):
        print("swim")


m = Mammal()
print(isinstance(m, object))
print(issubclass(Fish, object))
