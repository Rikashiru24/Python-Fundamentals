even_numbers = 0
for x in range(1, 10):
    if x % 2 == 0:
        even_numbers += 1
        print(x)
    else:
        print(f"Odd {x}")
        continue
print(f"We have {even_numbers} even numbers")
