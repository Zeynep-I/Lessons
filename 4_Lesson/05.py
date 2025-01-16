name = len(input("What's your name? "))
if name <= 4:
    print("Your name is short.")
elif name <= 6:
    print("Your name is a bit long.")
else:
    print("You have a very long name.")