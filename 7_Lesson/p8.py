n = int(input("Enter a number: "))
k = 1
while k <= n:
    if k % 2 == 0:
        print(f"{k} {'& ' * k}")
    else:
        print(f"{k} {'@ ' * k}")
    k += 1