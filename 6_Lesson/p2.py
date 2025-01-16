while True:    
    username = input("Please type new username: ")
    if len(username) >= 3 and  len(username) <= 15:
        print(f"Hi {username} :)")
        break
    else:
        print("Password legth must be between 3 - 15 symbols!")
       