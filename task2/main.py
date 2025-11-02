import random
rows = random.randint(4, 8)
cols = random.randint(4, 8)
values = [-3, -5, 2, 0, 1, 3, 4, 5, 6]
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        num = random.choice(values)
        row.append(num)
        print(f"{num:2}", end=" ")
    matrix.append(row)
    print()
total = sum(num for row in matrix for num in row if num % 3 == 0)
print("Сумма элементов, кратных 3:", total)