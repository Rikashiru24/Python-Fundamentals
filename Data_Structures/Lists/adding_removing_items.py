# How to add or remove item(s) in the list

letters = ["a", "b", "c"]

# ADD ITEM AT THE END OF THE LIST USING append() method
letters.append("d")
print(letters)  # ['a', 'b', 'c', 'd']

# ADD ITEM AT A SPECIFIC POSITION USING insert() method
letters.insert(0, "-")  # Add item at the very beginning, because of index 0
print(letters)  # ['-', 'a', 'b', 'c', 'd']

# REMOVING OBJECTs or Item
letters.pop()  # ['-', 'a', 'b', 'c']
letters.pop(0)  # ['a', 'b', 'c'], with a given index.
# if you don't know the index use remove() method: This will remove the first occurrence of the value.
letters.remove("b")
del letters[0:3]  # using del statement, we can remove a range of items.
letters.clear()  # Deleting all the objects in the list
print(letters)
