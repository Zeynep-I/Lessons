def login_system(dogry_ulanyjy, dogry_parol, max_gezek):
    gezek = 0
    while gezek < max_gezek:
        ulanyjy_ady = input("Ulanyjy adyny girizin: ")
        parol = input("Paroly girizin: ")
        if ulanyjy_ady == dogry_ulanyjy and parol == dogry_parol:
            print("Hos geldiiniz!")
            return
        else:
            gezek += 1
            print("Ulanyjy ady ya-da parol nadogry!")
    if gezek == max_gezek:
        print("Hasaba girmage mumkinciliginiz gutardy!")
login_system("user123", "parol1456", 3)