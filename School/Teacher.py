# Імпортуємо клас Student, щоб вчитель міг мати список студентів
from Student import Student

# Клас Teacher - це вчитель, який має ім'я, прізвище, вік, предмет та список студентів
class Teacher:

    # Конструктор - створює нового вчителя з його даними та порожнім списком студентів
    def __init__(self, first_name, last_name, age, subject):
        self.first_name = first_name  # ім'я вчителя
        self.last_name = last_name  # прізвище вчителя
        self.age = age  # вік вчителя
        self.subject = subject  # предмет, який викладає вчитель
        self.students = []  # список студентів вчителя
    # Метод __str__ - повертає текстове представлення вчителя
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.subject}"

    # Метод __lt__ - дозволяє порівнювати вчителів за віком (для сортування)
    def __lt__(self, other):
        return self.age < other.age

    # Метод додає студента до списку вчителя
    def add_student(self, student):
        self.students.append(student)

    # Метод виводить список всіх студентів вчителя
    def print_students(self):
        print(f"Учні на уроці вчителя: {self.first_name} {self.last_name} ")
        if not self.students:
            print("No students")
        else:
            for student in self.students:
                print(student.first_name, student.last_name)


# Створюємо 3 вчителів - кожен має ім'я, прізвище, вік та предмет, який викладає
teacher1 = Teacher("Roman", "Vodolaz", 32, "Swimming lesson")
teacher2 = Teacher("Nazar", "Barbos", 36, "Math")
teacher3 = Teacher("Yagon", "Don", 30, "Sport")

# Створюємо 7 студентів - кожен має ім'я, прізвище, вік та спеціальність
student1 = Student("Danya", "Varenik", 16, "Sport")
student2 = Student("Olena", "Shevchenko", 17, "Math")
student3 = Student("Maksym", "Bondarenko", 15, "Swimming lesson")
student4 = Student("Anastasia", "Koval", 16, "Sport")
student5 = Student("Dmytro", "Melnyk", 18, "Math")
student6 = Student("Sofia", "Tkachenko", 15, "Swimming lesson")
student7 = Student("Artem", "Kravchenko", 17, "Sport")

# Додаємо студентів до вчителів - кожен вчитель має своїх студентів
teacher1.add_student(student3)
teacher1.add_student(student6)
teacher2.add_student(student2)
teacher2.add_student(student5)
teacher3.add_student(student1)
teacher3.add_student(student4)
teacher3.add_student(student7)

# Створюємо список вчителів для роботи з ними
teacher_room = [teacher1, teacher2, teacher3]

# Функція знаходить вчителя за предметом
def find_teacher(teacher_room, subject_question):
    for teacher in teacher_room:
        if teacher.subject == subject_question:
            print(teacher.first_name, teacher.last_name)


# Функція виводить список вчителів, відсортованих за віком
def print_teacher(teacher_room):
    teacher_room.sort()  # сортуємо за віком (використовує __lt__)

    for teacher in teacher_room:
        print(teacher.first_name, teacher.last_name, teacher.age, teacher.subject)


# Коментований код - приклади використання функцій (розкоментуй для перевірки)
# print("Список викладачів:")
# print_teacher(teacher_room)
#
# print()
#
# print("Викладач предмета Math:")
# find_teacher(teacher_room, "Math")
#
# print()
#
# teacher1.print_students()
# print()
# teacher2.print_students()
# print()
# teacher3.print_students()
#
