num = int(input("uc belgili san girizin:\n"))
print(f"{num} -yn 1-nji sifri: { num // 100 }")
print(f"{num} -yn 2-nji sifri: { (num // 10) % 10 }")
print(f"{num} -yn 3-nji sifri: { num % 10 }")