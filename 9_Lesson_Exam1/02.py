k = 0
l = 0 
for i in range(1, 11):
    n = int(input(f"{i} - san yazyn: "))
    if n >= 0:
        k += n
    else:
        l += 1
print(f"Polozitel sanlaryn jemi: {k}")
print(f"Otrisatel sanlaryn mukdary: {l}")