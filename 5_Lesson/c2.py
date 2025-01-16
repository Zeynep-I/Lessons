n = int(input("Enter a number: "))
if n < 10 and n % 2 == 0:
    print("one digit, even")
elif n < 10 and n % 2 != 0:
    print("one digit, odd")
elif n < 100 and n % 2 == 0:
    print("two digit, even")
elif n < 100 and n % 2 != 0:
    print("two digit, odd")
elif n < 1000 and n % 2 == 0:
    print("three digit, even")
elif n < 1000 and n % 2 != 0:
    print("three digit, odd")
else:
    print("I didn't understand")