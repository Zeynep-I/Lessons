print("""<<< MENU >>>
1. Tea
2. Coffee
3. Water
4. Fruit juice""")
n = int(input("What would you like to drink? "))
if n == 1:
    print(f"You choice Tea")
elif n == 2:
    print(f"You choice Coffee")
elif n == 3:
    print(f"You choice Water")
elif n == 4:
    print(f"You choice Fruit juice")
else:
    print("I didn't understand")