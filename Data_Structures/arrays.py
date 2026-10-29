from array import array
# NOTE: https://docs.python.org/3/library/array.html ; to see the type-codes
numbers = array("i", [1, 2, 3])
# Every array should be the same-type, determined by the type-code in this case, 'i'
# numbers.append() # Append new value v to the end of the array.
# numbers.insert() # Insert a new item v into the array before position i.
# numbers.pop(4) # Return the i-th element and delete it from the array. i defaults to -1.
# numbers.remove(4) # Remove the first occurrence of v in the array.
# numbers[0] # Accessing item by index
# numbers[0] = 1.0 # TypeError: 'float' object cannot be interpreted as an integer
