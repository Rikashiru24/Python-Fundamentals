# Method Overriding = replacing or extending a method defined in the parent or base class

# Parent or Base Class
class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):  # This method overriding
       # super().__init__()  # To access and initialize the Animal method, using super() function
        print("Mammal Constructor")
        self.weight = 2
        # Without super(), we completely replace the __init__() method from the Animal parent class. Overridden by out Mammal __init__() method.
        super().__init__()  # To initialize first the Mammal before the Animal base class

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
