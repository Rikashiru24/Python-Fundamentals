# Multiple Inheritance

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


# Multiple Inheritance; In here, the first base class in parameter will be executed first.
# it becomes complicated when base classes have same method.
class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()


# GOOD EXAMPLE OF MULTIPLE INHERITANCE

class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


# A Flying fish is a flyer and a swimmer
class FlyingFish(Flyer, Swimmer):
    pass
