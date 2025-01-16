num = int(input("uc belgili san girizin:\n"))
a = num // 100 
b = (num // 10) % 10 
c = num % 10 
print(f"{num} -sanyn tersi: {c}{b}{a}")