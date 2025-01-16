phone_number = input("Enter your phone number: +993 ")
s = 0
while True:
    n = input("Please pay: ")
    if n == "quit":
        break
    else:
        s += int(n)
        print(f"You paid: {s} manats")   
print(f"{s} manats were trasferred to {phone_number}")