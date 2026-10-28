items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

# filtered = []

# for item in items:
#     filtered.append(item[1])

# for price in filtered:
#     if price >= 10:
#         print(f"The price is ${price}")
#     else:
#         print(f"The price is ${price}")

# To achieve the same, using built-in filter() function
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)  # [('Product1', 10), ('Product3', 12)]
