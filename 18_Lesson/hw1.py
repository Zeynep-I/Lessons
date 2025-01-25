def factorial(n):
    result = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n+1):
            result *= i
        return result
while True:
    number = int(input("Bir san girizin: "))
    if number < 0:
        print("Yalnys san! Pozitiw san girizin.")
        break
    else:
        last = factorial(number)
        print("Faktoriyal: ", last)