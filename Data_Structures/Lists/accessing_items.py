letters = ["a", "b", "c", "d"]
letters[0] = "A"
letters[0:3]  # ['A', 'b', 'c']
letters[::2]  # ['A', 'c']
letters[:]  # ['A', 'b', 'c', 'd']
letters[0:]  # ['A', 'b', 'c', 'd']
letters[:3]  # ['A', 'b', 'c']
letters[::]  # ['A', 'b', 'c', 'd']
letters[::-1]  # ['d', 'c', 'b', 'A']

numbers = list(range(20))
print(numbers[::-1])
