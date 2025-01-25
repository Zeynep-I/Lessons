def programma():
    balans = 5
    while True:
        print("""TMCell hyzmatlary
        1. Balansyny barlamak
        2. Balansyny doldurmak
        """)
        number = int(input("Hyzmat gornusini saylan (1, 2): "))
        if number == 1:
            telefon_belginiz = int(input("Telefon belginiz: "))
            if  telefon_belginiz >= 60000000 and telefon_belginiz <= 65999999 or telefon_belginiz >= 71000000 and telefon_belginiz <= 71999999: 
                print(f"Sizin balansynyz: {balans} tmt")
            else:
                print("Nadogry telefon belgi")
        elif number == 2:
            telefon_belginiz = int(input("Telefon belginiz: "))
            if telefon_belginiz >= 60000000 and telefon_belginiz <= 65999999 or telefon_belginiz >= 71000000 and telefon_belginiz <= 71999999: 
                manat = int(input("Toleg mocberiniz (tmt): "))
                if manat <= 50:
                    balans += manat
                    print(f"Sizin balansynyz: {balans} tmt")
                else:
                    print("Yalnys toleg mocberi yazdynyz!")
            else:
                print("Nadogry telefon belgi")
        elif number == 3:
            print("Sag bolun!")
            break
        else:
            print("Nadogry hyzmat sayladynyz!")
programma()