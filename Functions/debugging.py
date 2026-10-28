
"""
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        return total # This was the bug, indented into the for-loop
"""


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total  # Now the bug is fixed. Removing the indented space.


print("Start")
print(multiply(1, 2, 3))

"""
NOTE: To debug Python file, go to 'Run and Debug' and create launch.json. 
SELECT: 'Python Debugger: Current File'
NEXT: Create a breakpoint (Windows click F9, macOS click Fn + F9). It will show Red-Dot on the line where the cursor is.
NEXT: Click Fn + F5 or F5 only on window, to run the application up-to the Red-Dot. It will highlight the breakpoint.
NEXT: Execute the program, line-by-line to see what happens at Run-time, by Pressing Fn + F10. It will stop once the algorithm is done.
NEXT: To step into the function, press Fn + F11.
TO STOP DEBUGGER: Shift + F5
"""
