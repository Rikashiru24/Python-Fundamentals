items = [
    ('Product1', 10),
    ('Product2', 9),
    ('Product3', 12)
]

# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices) # [10, 9, 12]

# Using built-in map() function, we can achieve the same result
prices = list(map(lambda item: item[1], items))
# or prices = [i for i in map(lambda item: item[1], items)]
print(prices)
