
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didn't enter a valid age.")
else:  # This will only show when there's no exceptions
    print("No exceptions were thrown.")
print("Execution continues.")
