
message = "a"  # Global Variable


def greet(name):
    global message  # Modify the value, from "a" into argument of name parameter
    # Local Variable; Name for a variable within the function
    message = name
    return message


# Variables declared within the function is different from the Global Variable, even they've got the same same


print(greet("Harvin"))

print(message)  # It will no longer print 'a'
