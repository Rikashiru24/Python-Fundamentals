# and, all operands must be True
"""
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
"""

# or, at least only one from operands is True
"""
high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")
"""


# not, inverses the value of a boolean
high_income = False
good_credit = True
student = False

# At least only one True result from Parenthesis
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
