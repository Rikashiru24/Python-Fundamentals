# numbers = [3, 51, 2, 8, 6]
# numbers.sort()  # Sort the list in ascending order and return None. [2, 3, 6, 8, 51]
# numbers.sort(reverse=True) # [51, 8, 6, 3, 2]. Sorted in descending order.

# BUILT-IN FUNCTION sorted()
# print(sorted(numbers, reverse=True))  # [51, 8, 6, 3, 2]

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)  # [('Product2', 9), ('Product1', 10), ('Product3', 12)]
