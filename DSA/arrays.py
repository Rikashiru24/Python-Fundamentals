aggregation = []
concat = ""
is_continue = True
while is_continue:
    chars = input("Write a Letter: ")
    for char in chars:
        aggregation.append(char)
    print(concat.join(aggregation))
