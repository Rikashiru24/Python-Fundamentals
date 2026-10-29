# COST OF RAISING EXCEPTIONS
# When writing a functions, prefer not to raise exceptions; Because this exceptions comes with a costs.

from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print("Error")
"""

code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age



xfactor = calculate_xfactor(-1)

if xfactor == None:
    print("Error")

"""

# first code= 0.036935834000360046
print("first code=", timeit(code1, number=10000))
# second code= 0.02247945899989645
print("second code=", timeit(code2, number=10000))
