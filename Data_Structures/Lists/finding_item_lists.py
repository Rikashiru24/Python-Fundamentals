letters = ["a", "b", "c"]

# Finding index of a given object in a list using index() method
# If finding the non-existent object, we get ValueError: 'item' is not in list
# print(letters.index("d"))

# To prevent error from happening, first check if item does exist in the list using 'in' operator
if 'd' in letters:
    print(letters.index('d'))

# To count the occurrences of a given item, using count() method
print(letters.count('b'))
