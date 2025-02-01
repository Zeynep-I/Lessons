import random
A = ["Zeynep", "Ogulnur", "Aylar", "Melike", "Melek",]
print(random.choice(A), "\n")
print(random.sample(A, 3), "\n")
random.shuffle(A)
print(A)
