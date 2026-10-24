while True:
    command = input(">>")
    print("ECHO", command)
    if command.strip().lower() == "quit":
        break
