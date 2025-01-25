def hasap_barlamak(telefon_belginiz, balans):
    if (60000000 < telefon_belginiz < 65999999) or (71000000 < telefon_belginiz < 71999999): 
        print(f"Sizin balansynyz: {balans} tmt")
    else:
        print("Nadogry telefon belgi")
def hasap_doldurmak(telefon_belginiz, balans):
    if (60000000 < telefon_belginiz < 65999999) or (71000000 < telefon_belginiz < 71999999): 
        manat = int(input("Toleg mocberiniz (tmt): "))
        if 0 < manat < 50:
            balans += manat
            print(f"Sizin balansynyz: {balans} tmt")
        else:
            print("Yalnys toleg mocberi yazdynyz!")
    else:
        print("Nadogry telefon belgi")
balans = 5
while True:
    print("""
    TMCell hyzmatlary:
    1. Balansyny barlamak
    2. Balansyny doldurmak
        """)
    number = int(input("Hyzmat gornusini saylan (1, 2): "))
    if number == 1:
        telefon_belginiz = int(input("Telefon belginiz: "))
        hasap_barlamak(telefon_belginiz, balans)
    elif number == 2:
        telefon_belginiz = int(input("Telefon belginiz: "))
        hasap_doldurmak(telefon_belginiz, balans)
    elif number == 3:
        print(" Programma tamamlandy")
        break
    else:
        print(" Nadogry hyzmat sayladynyz! ")