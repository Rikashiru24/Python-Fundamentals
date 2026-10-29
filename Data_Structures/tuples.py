# Tuples - Read-only list, contains sequence of object; cannot modify, add and remove.

point = (1, 2, 3, 4)

print(point[0:2])
x, y, z, *other = point
if 10 in point:
    print("exists")
