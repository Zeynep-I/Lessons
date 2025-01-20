fruits = {
    "alma" : {
        "bahasy" : 15,
        "mukdary" : 30,
    },
    "mandarin" : {
        "bahasy" : 30,
        "mukdary" : 10,
    },
    "kivi" : {
        "bahasy" : 18,
        "mukdary" : 1,
    },
    "banan" : {
        "bahasy" : 27,
        "mukdary" : 20,
    },
    "nar" : {
        "bahasy" : 18,
        "mukdary" : 15,
    }
}
while True:
    print("""*** DUKAN DOLANDYRYSY ***
    1 - Harytlary gorkezmek. 
    2 - Haryt satyn almak. 
    3 - Taze haryt gosmak. 
    4 - Harydyn bahasyny uytgetmek. 
    5 - Harydy ayyrmak. 
    6 - Mukdary artdyrmak. 
    7 - quit.
    """)
    isleg = int(input("isleg: "))
    if isleg == 1:
        print("Harytlar")
        for i,j in fruits.items():
            print(i, " - " , j, "\n")
    elif isleg == 2:
        fruit = input("Haýsy harydy satyn almak isleýän: ")
        if fruit in fruits:
            mukdar = int(input("satyn almak isleýän mukdaryn: (kg) "))
            if mukdar <= fruits[fruit]["mukdary"]:
                fruits[fruit]["mukdary"] -= mukdar
                baha = mukdar * fruits[fruit]["bahasy"]
                print(f"Siz {baha} manat tolemeli")
            else:
                print("Yeterlik mukdarda yok")
        else:
            print("Dukanda yok!")
    elif isleg == 3:
        fruit = input("Girizmek isleyan mive: ")
        bahasy = int(input("Bahasy: "))
        mukdary = int(input("Mukdary: "))
        fruits[fruit] = {"bahasy" : bahasy, "mukdary" : "mukdary"}
        print("Taze haryt gosuldy!")
    elif isleg == 4:
        fruit = input("Harydyn ady: ")
        if fruit in fruits:
            bahasy = int(input("Harydyn taze bahasy: "))
            fruits[fruit]["bahasy"] = bahasy
        else:
            print("Dukanda yok!")
        print("Harydyn bahasy uytgedildi!")
    elif isleg == 5:
        fruit = input("Harydyn ady: ")
        fruits.pop(fruit)
        print("Haryt ayyrylyldy!")
    elif isleg == 6:
        fruit = input("Mukdary ayyrmak isleyan harydyn ady: ")
        mukdary = int(input("Mukdary: "))
        fruits[fruit]["mukdary"] -= mukdary
        print("Mukdara azaldyldy")
    elif isleg == 7:
        fruit = input("Mukdary kopeltmek isleyan harydyn ady: ")
        mukdary = int(input("Mukdary: "))
        fruits[fruit]["mukdary"] += mukdary
        print("mukdar kopeldildi")
    elif isleg == 8:
        break