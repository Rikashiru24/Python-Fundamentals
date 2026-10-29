# TASK: Write a program to find the most repeated character in the string.

from pprint import pprint
sentence = "This is a common interview question"

# visited = set()
# common_char = dict()
# for char in sentence:
#     if char not in visited:
#         visited.add(char)
#         common_char[char] = 1
#     else:
#         common_char[char] += 1


# print(common_char)


char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1


char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_frequency_sorted[0])  # ('i', 5)
