# Generators - doesn't store all values in memories, they generate a new value in each iteration

from sys import getsizeof

# 1000 > gen:  208 bytes, 100,000 > gen:  208 bytes ; remains the same size.
# GENERATOR EXPRESSION
values = (x * 2 for x in range(100000))
print("gen: ", getsizeof(values))


# print(values) # <generator object <genexpr>
# for x in values:
#     print(x)
