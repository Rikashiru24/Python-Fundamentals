# Class: blueprint for creating new objects
# Object: instance of a class
# Naming a class uses Pascal-naming convention; First letter of every word in Upper case, with no separation.


class Point:
    def draw(self):
        print("draw")


# Creating point object
point = Point()
print(type(point))
print(isinstance(point, Point))
