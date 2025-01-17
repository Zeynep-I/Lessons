students = {
    "Anna" : {
        "synag1" : "65",
        "synag2" : "93",
        "synag3" : "88"
    },
    "Merdan" : {
        "synag1" : "100",
        "synag2" : "100",
        "synag3" : "98"
    },
    "Oraz" : {
        "synag1" : "74",
        "synag2" : "77",
        "synag3" : "89"
    }
}
print(students["Merdan"])
print(students["Anna"]["synag1"])
print(students["Oraz"]["synag3"])
ady = input("Ady: ")
if ady in students:
    isleg = input("Ahli synaglar:(Hava/Yok) ")
    if isleg == "Hava":
        print(students[ady])
    else:
        synag = input("synag1/synag2/synag3: ")
        print(students[ady][synag])
else:
    print(f"{ady} atly okuvcy yok")
