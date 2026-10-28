letters = ["a", "b", "c"]

for letter in letters:
    print(letter)

# GETTING THE INDEX AS WELL USING enumerate() that returns a tuple
for letter in enumerate(letters):
    print(letter)
    # (0, 'a')
    # (1, 'b')
    # (2, 'c')

# To unpack a tuple
items = (0, "a")
index, letter = items

for index, letter in enumerate(letters):
    print(index, letter)
    # 0 a
    # 1 b
    # 2 c
