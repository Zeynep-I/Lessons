num = int(input("Iki belgili san girizin:\n"))
a = num // 10 
b = num % 10
print(f"{num} - sanyn sifrlerinin jemi: { a + b }")
print(f"{num} - sanyn kop.has: { a * b }")