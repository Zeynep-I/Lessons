print("The price of 0.5 Pepsi is 5 manats")
s = 0
while True:
    if s == 5:
        break
    else:
        n = float(input("Please pay: "))
        s += n
        print(f"You paid: {s} manats")
    
print(f"Take a 0.5 Pepsi")