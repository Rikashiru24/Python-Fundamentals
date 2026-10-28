list1 = [1, 2, 3]
list2 = [10, 20, 30, 40]

# TASK: Combined lists into this [(1, 10), (2, 20), (3, 30)]. Using built-in zip() function

print(list(zip(list1, list2)))  # [(1, 10), (2, 20), (3, 30)]
# or we can add more different iterables
# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
print(list(zip("abc", list1, list2)))
