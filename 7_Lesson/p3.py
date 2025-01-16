n = int(input("Enter a number: "))
while n >= 1:
    if n % 2 == 0:
        print(f"{n} is a even number")
    else:
        print(f"{n} is a odd number")
    n -= 1
