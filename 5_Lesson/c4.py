n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))
if n1 < n2 and n2 < n3:
    print(f"Mid number:{n2}")
elif n2 < n3 and n3 < n1:
    print(f"Mid number:{n3}")
else:
    print(f"Mid number:{n1}")