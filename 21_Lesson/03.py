import random
computer1 = 0
player1 = 0
while True:
    a = input("Do you roll a dice? (yes / no): ")
    if a == "yes":
        computer = random.randint(1, 6)
        player = random.randint(1, 6)
        print(f"Computer: {computer}")
        computer1 += computer
        print(f"Player: {player}")
        player1 += player
    else:
        print("* * * * * FINAL SCORE * * * * *")
        print(f"Computer: {computer1}")
        print(f"Player: {player1}")
        if computer1 < player1:
            print("Congratulations you won")
        else:
            print("You lose")
        break