from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, value):  # compare the true value of each attributes.
        return self.x == value.x and self.y == value.y


# p1 = Point(1, 2)
# p2 = Point(1, 2)

# print(p1 == p2)
# print(id(p1))
# print(id(p2))

# if classes contains only data, not behavior do this. using namedtuple() function
# In this way no need to explicitly implement __eq__ magic method, to compare them.
# Use only namedtuple() instead, when classes contains only data and no method or behavior.
# namedtuple() is immutable; can't set attribute
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1.x)
print(p1.y)
print(p1 == p2)

# To modify attribute with new value, need to create a Point object
p1 = Point(x=3, y=4)
print(p1.x)
print(p1.y)
