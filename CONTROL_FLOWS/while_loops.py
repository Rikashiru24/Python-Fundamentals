# While Loop: Repeats something as long as the condition is True.

"""
number = 100
while number > 0:
    print(number)
    number //= 2
"""

command = ""

while command.strip().lower() != "quit":
    command = input(">>")
    print("ECHO", command)
