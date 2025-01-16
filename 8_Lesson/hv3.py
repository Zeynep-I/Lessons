n = int(input("How many numbers input: "))
s = 0
for i in range(1, n+1):
    k = int(input(f"{i} number: "))
    s += k
print(f"Sum: {s}")