# USING LIST COMPREHENSION COMPARED TO MAP FUNCTION AND FILTER FUNCTION

items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)  # [10, 9, 12]

# filtered = list(filter(lambda item: item[1] >= 10, items))
prices = [item for item in items if item[1] >= 10]
print(prices)  # [('Product1', 10), ('Product3', 12)]
