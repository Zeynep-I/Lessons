numbers = [1, 2, 3, 4, 5, 6]
A = []
B = []
for i in numbers:
    if i % 2 == 0:
        A.append(i)
    else:
        B.append(i)
print(f"Jubut sanlar: {A}, Tak sanlar: {B}")