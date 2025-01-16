print("""
    1. ( + )
    2. ( - )
    3. ( * )
    4. ( / )   
""")
n = input("Haysy amal: ")
a = int(input("1-nji san: "))
b = int(input("2-nji san: "))
if n == "+":
    print(f"{a} + {b} = {a + b}")
elif n == "-":
    print(f"{a} - {b} = {a - b} ")
elif n == "*":
    print(f"{a} * {b} = {a * b} ")
elif n == "/":
    print(f"{a} / {b} = {a / b} ")