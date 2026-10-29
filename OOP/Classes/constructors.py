# __init__ - is a magic method
# self - is the reference to the current point object

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}), ({self.y})")


# Creating point object
point = Point(1, 2)
point.draw()
