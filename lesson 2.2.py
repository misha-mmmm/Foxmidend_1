import os

filename = input("Введіть імя файлу в який хочете записати пацієнтів: ")
if not os.path.exists(filename):
    print(f"File {filename} not found")
    open(filename, "w")
    print(f"New {filename} maked")
else:
    print(f"File {filename} found")



if not filename.endswith(".txt"):
    print(f"File {filename} must end with .txt")
    exit()


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


    for patient in patients:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Ім'я: {patient[0]}, Прізвище: {patient[1]}, Вік: {patient[2]} \n")
        # file.close()



