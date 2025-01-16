n = int(input("Enter a number of temperature: "))
if n < 0:
    print("Freezing weather")
elif n >= 1 and n <= 10:
    print("Very cold weather")
elif n >= 11 and n <= 20:
    print("Cold weather")
elif n >= 21 and n <= 30:
    print("Normal")
elif n >= 31 and n <= 40:
    print("Hot")
else:
    print("Very hot")