numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# BETTER WAY TO UNPACKED IT; This is called List-Unpacking
# To unpack, the variables must be the same to that length values of the list
# What if only the first and second we want, then we packed others with new variable but with trailing asterisk *
first, second, *other = numbers
print(first, second, other)  # 1 2 [3, 4, 5, 6, 7, 8, 9]

# now to get the first and last items only
first, *other, last = numbers
print(first, other, last)  # 1 [2, 3, 4, 5, 6, 7, 8] 9
