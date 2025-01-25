def min_max_numbers():
    num = int(input("Bir san girizin (Durmak ucin 0): "))
    if num == 0:
        print("San girizilmedi!")
    else:
        max_num = num
        min_num = num
        while True:
            num = int(input("Bir san girizin (Durmak ucin 0): "))
            if num > max_num:
                max_num = num
            if num < min_num and num != 0:
                min_num = num
            if num == 0:
                print(f"In uly san: {max_num},    In kici san: {min_num}")
                break
min_max_numbers()