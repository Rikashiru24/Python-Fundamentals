numbers = [1, 2, 3]
print(*numbers)  # unpacking operator using asterisk returns 1 2 3

values = list(range(5))
# Without using list() function, but unpacking operator only
values = [*range(5), *"Hello"]  # [0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']
print(values)

# Combining lists using unpacking operator
first = [1, 2]
second = [3]
combined_lists = [*first, *second]  # [1, 2, 3]
print(combined_lists)

# Unpacking dictionaries using unpacking operator, using ** double asterisks
first_dict = {"x": 1}
second_dict = {"x": 10, "y": 2}
combined_dicts = {**first_dict, **second_dict}  # {'x': 10, 'y': 2}
print(combined_dicts)
# NOTE: If you have the multiple same key in dict, the last value will be used.
