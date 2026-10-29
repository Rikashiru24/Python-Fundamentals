
# values = []
# for x in range(5):
#     values.append(x * 2)


# # Using list comprehension to achieve the same thing
# values = [x * 2 for x in range(5)]
# print(values)  # [0, 2, 4, 6, 8]

# Set Comprehension
# values = {x * 2 for x in range(5)}
# print(values) # {0, 2, 4, 6, 8}

# Dict Comprehension
values = {x: x * 2 for x in range(5)}
print(values)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}

# Simplification of Dict Comprehension
values = {}

for x in range(5):
    values[x] = x * 2

print(values)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
