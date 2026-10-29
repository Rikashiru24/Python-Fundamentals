class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)

# False ; Equality operator, compares the addresses in memory
# After implementing __eq__ magic method we get True
# print(point == other)
# print(point > other)
# False; no need to implement __lt__ method, since we've already have __gt__
print(point < other)
