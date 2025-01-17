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
baha = 0
while True:
    for i,j in fruits.items():
        print(i, " - " , j, "\n")
    fruit_name = input("Name almak isleyarsiniz? ")
    if fruit_name in fruits:
        mukdar = float(input("Nache kg almak isleyarsiniz? "))
        if mukdar <= fruits[fruit_name]["mukdary"]:
            fruits[fruit_name]["mukdary"] =  fruits[fruit_name]["mukdary"] - mukdar
            baha += mukdar * fruits[fruit_name]["bahasy"]
            for i,j in fruits.items():
                print(i," - ", j)
        else:
            print("Yeterlik mukdarda yok!\n")
    elif fruit_name == "quit":
        break
    else:
        print(f"{fruit_name} dukanda yok!\n")
print(f"Siz {baha} manat tolemeli")