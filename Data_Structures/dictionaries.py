# Dictionary - A collection of key: value pairs. e.g., {"key": value}

point = {"x": 1, "y": 2}

# dict() function
point = dict(x=1, y=2)
# print(point["x"])  # 1
point["x"] = 10  # {'x': 10, 'y': 2}
point["z"] = 20  # adding new key: value pair; {'x': 10, 'y': 2, 'z': 20}

# When accessing non-existent key we'll get--KeyError: 'a'
# print(point["a"]) # KeyError: 'a'

# To check first the existence
if "a" in point:
    pass
    # print(point["a"])  # Doesn't return an error

# To achieve the same thing, use get() method
# print(point.get("a"))  # If key doesn't exists, by default it will return 'None'
# or we can pass a default value as a second argument
# print(point.get("a", 0))  # returns 0

# To delete an item, use del statement
# del point["x"]
# print(point) # {'y': 2, 'z': 20}

# Looping over dictionaries
for key in point:
    print(key, point[key])
# x 10
# y 2
# z 20

# Another way to iterate dictionaries
for x in point.items():
    print(x)
# ('x', 10)
# ('y', 2)
# ('z', 20)

# To extract it
for key, value in point.items():
    print(key, value)
# x 10
# y 2
# z 20
