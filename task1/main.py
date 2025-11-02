lines = ["весна" , "мечта" , "скамейка" , "полночь", "закат", "дождь"]
count = 0 
for line in lines:
   if 'в' in line:
    count += 1
print("количество строк, содержащих букву 'в' =" , count)