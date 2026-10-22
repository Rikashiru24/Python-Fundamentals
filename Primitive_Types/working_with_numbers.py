import math

# USEFUL FUNCTIONS TO WORK WITH NUMBERS

# Round-down when decimal is 5 and below; Round-up when decimal is 5 and above
print(round(2.5))
# Always remove the (-) sign.
print(abs(-1.0))


# Moving right on the number line (away from zero)
print(math.ceil(4.1))   # Outputs: 5   (Rounds UP / Right)
print(math.ceil(4.9))   # Outputs: 5   (Rounds UP / Right)

# Already on a whole integer boundary
print(math.ceil(4.0))   # Outputs: 4   (Stays unchanged)

# Moving right on the number line (toward zero)
print(math.ceil(-4.2))  # Outputs: -4  (Rounds UP / Right)

print(math.floor(2.2))  # Outputs: 2 (rounds DOWN)
