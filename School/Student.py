# Клас Student - це студент, який має ім'я, прізвище, вік та спеціальність
class Student:

    # Конструктор - створює нового студента з його даними
    def __init__(self, first_name, last_name, age, major):

        self.first_name = first_name  # ім'я студента
        self.last_name = last_name  # прізвище студента
        self.age = age  # вік студента
        self.major = major  # спеціальність студента


# Створюємо тестового студента для перевірки
student1 = Student("Ivan", "Petrenko", 20, "Computer Science")