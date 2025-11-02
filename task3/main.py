n = int(input("Сколько строк? "))
text = ""
for _ in range(n):
    text += input() + " "


words = text.split()
unique = set(words)
print("Разных слов:", len(unique))