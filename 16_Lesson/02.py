Kitap = {
    101 : {
        "ady" : "Perman",
        "awtory" : "A.Govshudov",
        "sany" : 8,
    },
    102 : {
        "ady" : "Saylanan eserler",
        "awtory" : "G.Ezizov",
        "sany" : 12,
    },
    103 : {
        "ady" : "Ykbal",
        "awtory" : "H.Deryayev",
        "sany" : 6,
    },
    104 : {
        "ady" : "Leyli Mejnun",
        "awtory" : "N.Andalyp",
        "sany" : 4,
    },
    105 : {
        "ady" : "Oylanma bayry",
        "awtory" : "K.Gurbannepesov",
        "sany" : 9,
    }
}
while True:
    print("""
    * * * * * KITAPHANA * * * * *
    1. Kitaplary gormek.
    2. Kitaplary almak.
    3. Kitap tabshyrmak.
    4. Cykmak.
    """)
    san = int(input("Saylan: "))
    if san == 1:
        for i,j in Kitap.items():
            print(i, " - " , j, "\n")
    elif san == 2:
        kitap_belgisi = int(input("Kitap belgisi: "))
        if kitap_belgisi in Kitap:
            kitap_sany = int(input("Kitap sany: "))
            if kitap_sany != 0:
                print(f"Siz {Kitap[kitap_belgisi]['awtory']} - yn {Kitap[kitap_belgisi]['ady']} kitabyndan {kitap_sany} sany aldynyz!")
                Kitap[kitap_belgisi]['sany'] -= kitap_sany
            else:
                print("Kitap wagtlacynca yok!")
        else:
            print(f"{kitap_belgisi} belgide kitap yok!")
    elif san == 3:
        kitap_belgisi = int(input("Kitap belgisi: "))
        if kitap_belgisi in Kitap:
            kitap_sany = int(input("Kitap sany: "))
            print(f"Siz {Kitap[kitap_belgisi]['awtory']} - yn {Kitap[kitap_belgisi]['ady']} kitabyndan {kitap_sany} sany tabshyrdynyz!")
            Kitap[kitap_belgisi]['sany'] += kitap_sany
        else:
            print(f"{kitap_belgisi} belgide kitap yok!")
    elif san == 4:
        print("Sag bolun, Kitaphana gelip durun!")
        break
    else:
        print("Nadogry buyruk!")
        break
