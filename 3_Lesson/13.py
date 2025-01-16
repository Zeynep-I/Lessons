price = float(input("Price: "))
tl = float(input("1 TL: "))
Weight = float(input("Weight: "))
kg = float(input("1 KG: "))
a = price * tl
b = Weight * kg
print(20 * "-")
print(f"Money due: {a + b} manats")