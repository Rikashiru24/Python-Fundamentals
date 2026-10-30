# Multi-Level Inheritance = Linear Chain; Grandparent ➔ Parent ➔ Child


class Animal:
    def eat(self):
        print("Eat")


class Bird(Animal):
    def fly(self):
        print("Fly")


class Chicken(Bird):
    pass

# NOTE: Best practice to limit at least two classes of Multi-Level Inheritance only.
# If a class inherit method(s) that doesn't need, it is inheritance abused.
