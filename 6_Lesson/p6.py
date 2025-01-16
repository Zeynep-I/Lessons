k = 0
l = 0
while True:    
    n = int(input("Enter a number: "))
    if n == 0:
        break
    elif n >= 40:
        k += n
        l += 1
print(f"{(k * 100 // l) // 100} percent of students are passed exam!")
       