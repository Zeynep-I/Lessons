Okuvchylar = {}
Okuvchylar.setdefault("Nurberdi", 17)
Okuvchylar.setdefault("Batyr", 15)
Okuvchylar.setdefault("Selim", 12)
print(Okuvchylar, "\n")

Okuvchylar['Nurberdi'] = 18
print(Okuvchylar, "\n")

Okuvchylar.pop('Batyr')
print(Okuvchylar, "\n")

keys = []
values = []
for i,j in Okuvchylar.items():
    keys.append(i) 
    values.append(j)
print(f"dict_keys({keys}) \n")
print(f"dict_values({values}) \n")