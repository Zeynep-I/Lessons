n = int(input("Enter a number: "))
if n > 0 and n % 2 == 0:
    print("Positive, even")
elif n > 0 and n % 2 != 0:
    print("Positive, odd")
elif n < 0 and n % 2 == 0:
    print("Negative, even")
elif n < 0 and n % 2 != 0:
    print("Negative, odd")
else: 
    print("Zero")
