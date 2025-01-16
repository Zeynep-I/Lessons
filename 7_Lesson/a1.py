print("""
    1. ( ** )
    2. ( % )
    3. ( // )
    4. ( ** 0.5 )
    5. Exit
""")

while True:
    n = int(input("haysy amal: "))

    if( n == 5):
        break
    elif ( n == 1 ):
        n1 = int(input("girizjek sanyn: "))
        n2 = int(input("girizjek derejan: "))
        print(f"{n1} - in {n2} -nji derejesi: {n1 ** n2}")
    elif ( n == 2 ):
        n1 = int(input("1 - nji girizjek sanyn: "))
        n2 = int(input("2 - nji girizjek sanyn: "))
        print(f"{n1} - in {n2} -e boleninde galyndysy: {n1 % n2}")
    elif ( n == 3 ):
        n1 = int(input("girizjek sanyn: "))
        n2 = int(input("girizjek derejan: "))
        print(f"{n1} - in {n2} -nji derejesi: {n1 ** n2}")
    elif ( n == 4 ):
        n1 = int(input("girizjek sanyn: "))
        n2 = int(input("girizjek derejan: "))
        print(f"{n1} - in {n2} -nji derejesi: {n1 ** n2}")
