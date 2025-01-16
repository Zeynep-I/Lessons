while True:    
    password = input("Please type new password: ")
    if len(password) >= 8:
        print("Accepted password")
        break
    else:
        print("Password legth must be at least 8 symbols!")
       