x = 10
y = 11

# z = x
# x = y
# y = z
# print("x: ", x, "y: ", y)

# Another way to do it

x, y = y, x  # Defining a tuple, and unpacking it on the left-side and assign.
# Interpretation: x, y = (11, 10)
print("x: ", x, "y: ", y)
