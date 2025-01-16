print("""
    1. ( + )
    2. ( - )
    3. ( * )
    4. ( / )   
""")
n = int(input("\nHaysy amal: "))
a = int(input("\n1-nji san: "))
b = int(input("\n2-nji san: \n"))
if n == 1:
    print(f"{a} + {b} = {a + b}")
elif n == 2:
    print(f"{a} - {b} = {a - b} ")
elif n == 3:
    print(f"{a} * {b} = {a * b} ")
elif n == 4:
    print(f"{a} / {b} = {a / b} ")