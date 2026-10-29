# Class Methods - cls by convention parameter
# Instance Methods - self by convention parameter
# @classmethod - A decorator, a way to extend the behavior of a function
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):  # Class Method
        return cls(0, 0)  # This will be pass like Point(0, 0)

    def draw(self):  # Instance Method
        print(f"Point ({self.x}), ({self.y})")


point = Point.zero()  # Class Level Method or Factory Method
point.draw()
