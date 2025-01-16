n = int(input("Enter your score: "))
if n > 100 or n < 0:
    print("Please enter between 100 and 0 ")
elif n >= 90:
    print("A")
elif n >= 80:
    print("B")
elif n >= 70:
    print("C")
elif n >= 60:
    print("D")
elif n >= 40:
    print("E")
else:
    print("F")