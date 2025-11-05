import random
groups = [[random.randint(-10, 10) for _ in range(4)] for _ in range(20)]
unique = list({tuple(sorted(g)) for g in groups})
print("Уникальные комбинации:")
for u in unique:
    print(u)
a = int(input("\nВведите целое число = "))
flat = [x for g in groups for x in g]
count = sum(1 for i in range(len(flat)) for j in range(i + 1, len(flat)) if flat[i] + flat[j] < a)
print(f"\nКоличество пар с суммой меньше {a}: {count}")

