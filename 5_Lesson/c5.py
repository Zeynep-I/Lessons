a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = b ** 2 - ( 4 * a * c)

if d > 0:
    print(f" x1 = {(-b + (d ** 0.5)) / (2 * a)} \n x2 = {(-b - (d ** 0.5)) / (2 * a)}")
elif d == 0:
    print(f" x1 = {-b / (2 * a)}")
else:
    print("No roots")