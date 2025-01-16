k = 0
l = 0
while True:    
    n = int(input("Enter a number: "))
    if n == 0:
        break
    else:
        k += n
        l += 1
print(f"Avarage: {k / l}")
       