polozitel = []
otrisatel = []
with open("Numbers.txt", "r") as file:
    a = file.read().split()
    for i in a:
        if int(i) > 0:
            polozitel.append(int(i))
        else:
            otrisatel.append(int(i))

with open("Polozitel.txt", "w") as file:
    for i in polozitel:
        file.write(str(i) + "\t") 
with open("Otrisatel.txt", "w") as file:
    for i in otrisatel:
        file.write(str(i) + "\t") 
    