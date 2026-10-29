# Sets - doesn't store duplicate items--only unique items. Unordered collections.
# To define sets, use curly-braces. Cannot Access them using an index

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
# second.add(5)
# # Remove an element from a set; it must be a member. If the element is not a member, raise a KeyError.
# second.remove(5)
# len(second)
# print(unique)  # {1, 2, 3, 4} ; duplicated 1 was removed.

# | union of sets ; includes items that are either in first set or second set
print(first | second)  # {1, 2, 3, 4, 5}
# & Intersection of sets ; returns items that are in both first and second sets
print(first & second)  # {1}
# - Difference of sets ; returns first set items that are not in second set
print(first - second)  # {2, 3, 4}
# ^ Symmetric Difference of sets ; returns an items that are either in the first or second set but not both
print(first ^ second)  # {2, 3, 4, 5}

if 1 in first:
    print("Yes")
