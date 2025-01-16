n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))
if n1 < n2 and n2 > n3:
    print(f"Min number: {n3} \n Max number: {n1}")
elif n2 < n3 and n3 > n1:
    print(f"Min number: {n1} \n Max number: {n3}")
elif n3 < n1 and n1 > n2:
    print(f"Min number: {n2} \n Max number: {n3}")
    