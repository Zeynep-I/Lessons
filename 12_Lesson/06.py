A = ["The", "quick", "brown", "fox", "jumps", "of"]
B = []
for i in A:
    if len(i) > 3:
        B.append(i)
print(B)