k = int(input("Toparda nace adam bar?: "))
gecen = 0
gecmedik = 0
jemi = 0
for i in range (1, k + 1):
    n = int(input(f"{i} - okuvcynyn synag bahasy: "))
    if n >= 50:
        gecen += 1
        jemi += n
    else:
        gecmedik +=1 
        jemi += n
print(f"Synagdan gechen okuvchylaryn sany: {gecen}")
print(f"Synagdan gechmedik okuvchylaryn sany: {gecmedik}")
print(f"Toparyn ortaca bahasy: {jemi // k}")