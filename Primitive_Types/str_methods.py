# CASE METHOD, MODIFY LETTERS
case_course = "Python Programming"
print(case_course.upper())  # return new string, original string retained.
print(case_course.lower())
print(case_course.title())


# STRIP METHOD, REMOVE WHITE SPACES (BOTH BEGINNING AND END)
strip_course = " Python Programming "
print(strip_course.strip())  # remove white-spaces from both ends
print(strip_course.lstrip())  # remove white-space at the left-end
print(strip_course.rstrip())  # remove white-space at the right-end


# FIND METHOD, CASE-SENSITIVE. -1 NOT FOUND
find_course = "Python programming"
print(find_course.find("pro"))  # return the index of a substring

# REPLACE METHOD
replace_course = "Python Programming"
# modify with "J" all the occurrences of "P" in a string
print(replace_course.replace("P", "J"))
# modify with "J" all to the end, the occurrences of "P" in a string
print(replace_course.replace("P", "J", -1))
# modify with "J" only the first occurrence of "P" in a string
print(replace_course.replace("P", "J", 1))
# modify nothing, since third argument is 0
print(replace_course.replace("P", "J", 0))
# modify with "J" all the first two occurrences of "P" in a string
print(replace_course.replace("P", "J", 2))


# IN OPERATOR, CHECKING THE EXISTENCE OF A CHARACTER IN A STRING
in_course = "Python Programming"
print("Pro" in in_course)  # return boolean value; case-sensitive

# NOT OPERATOR, CHECK IF STRING DOESN'T CONTAIN THE CHARACTER
not_course = "Python Programming"
print("Pro" not in not_course)  # return boolean value
