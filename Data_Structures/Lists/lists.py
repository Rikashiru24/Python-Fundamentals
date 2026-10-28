"""
NOTE: List can store different-types of values.
We can combine list of numbers and list of letters or boolean
"""

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
print(combined)


"""
CREATING A LIST OF NUMBERS FROM 0-20, USING LIST FUNCTION AND ITERABLES WHICH IS RANGE()
"""
numbers = list(range(20))
chars = list("Hello World")
print(chars)

"""
USING LEN() FUNCTION, WE CAN COUNT THE VALUES
"""

print(len(chars))
