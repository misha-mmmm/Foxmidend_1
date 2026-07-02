tekst = input("Введіть рядок для аналізу: ")
total_chars = len(tekst)
set_tekst = set(tekst)

print("Результат аналізу:")
print("| символ | частота |")
print("|--------|----------|")

for item in set_tekst:
    count = tekst.count(item)
    frequency = count / total_chars
    print(f"|   {item}    | {frequency:.3f}   |")

print("|--------|----------|")
