numbers = []
with open("Sanlar.txt", "r") as file:
    a = file.read().split()
    for i in a:
        numbers.append(int(i))

max_num = max(numbers)
min_num = min(numbers)
total = sum(numbers)
average = total / len(numbers)

with open("Sanlar2.txt", "w") as file:
    file.write(f"In uly san: {max_num} \n")
    file.write(f"In kici san: {min_num} \n")
    file.write(f"Jemi: {total} \n")
    file.write(f"Ortaca baha: {average} \n")