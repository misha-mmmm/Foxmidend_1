patients = []

while True:
    print("Для вводу наступного користувача натисніть Enter, для завершення введення введіть 'q':")
    command = input()

    if command == 'q':
        break

    name = input("Введіть ім'я користувача: ")
    surname = input("Введіть прізвище користувача: ")
    age = int(input("Введіть вік користувача: "))

    patient = [name, surname, age]
    patients.append(patient)

print()

for patient in patients:
    print(f"Ім'я: {patient[0]}, Прізвище: {patient[1]}, Вік: {patient[2]}")
