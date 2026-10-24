
high_income = False
good_credit = True
student = True

# The evaluation stops, as soon as one of the argument evaluate to False.
if high_income and good_credit and not student:
    print("Eligible")

# The evaluation stops, as soon as it finds arguments evaluate to True.
if high_income or good_credit or not student:
    print("Eligible")

# In conclusion, Logical Operators in Python are Short-Circuit
