import random
numbers = [random.randint(-50, 50)for _ in range(25)  ]
pos = len ([ x for x in numbers if x > 0])
neg = len ([x for x in numbers if x < 0])
zero = len ([x for x in numbers if x == 0])
total = len(numbers)
min_val = min(numbers)
max_val = max(numbers)
print(numbers)
print(f"polozitelnie ={pos} ({pos/total*100:.1f}%)")
print(f"отрицательные = {neg} ({pos/total*100:.1f}%)")
print(f"Нулевые = {zero} ({pos/total*100:.1f}%)")
print(total)

print(f"MAX:{max_val} , MIN:{min_val}")

 
