
# Instance Attributes - are independent and uniquely-attribute to each objects or of instance
# Class Attributes - Shared across all instances of a class.

class Point:
    default_color = "red"  # Class level attribute

    def __init__(self, x, y):
        self.x = x  # Instance attributes
        self.y = y  # Instance attributes

    def draw(self):
        print(f"Point ({self.x}), ({self.y})")


Point.default_color = "yellow"

point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.draw()
another = Point(3, 4)
print(another.default_color)
print(Point.default_color)
another.draw()
