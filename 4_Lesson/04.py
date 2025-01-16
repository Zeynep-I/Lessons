score = int(input("Your score: "))
if score > 100 or score < 0:
    print("Invalid score.")
elif score >= 90 and score <= 100:
    print("You got an A.")
elif score >= 80 and score <= 89:
    print("You got a B.")
elif score >= 70 and score <= 79:
    print("You got a C.")
elif score >= 60 and score <= 69:
    print("You got a D.")
elif score >= 0 and score <= 59:
    print("You got an F.")