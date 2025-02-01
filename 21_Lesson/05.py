print(f"""
Jemi 10 sorag
""")

import random
jem1 = 0
jem2 = 0

for i in range (1, 11):
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    print(f"{i} - nji sorag\n{a} + {b} = ?")
    jogap = int(input("Your answer: "))
    if jogap == a + b:
        print("Corrrect")
        jem1 += 1
    else:
        print(f"Your answer is incorrect. Correct answer is {a + b}")
        jem2 += 1
print("* * * YOUR RESULT * * *")
print("question: 10")
print(f"Correct answer: {jem1}")
print(f"Incorrect answer: {jem2}")
print(f"{jem1 * 100 / 10} %")