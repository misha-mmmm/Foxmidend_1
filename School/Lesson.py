# Імпортуємо класи, які потрібні для створення уроку
from Teacher import Teacher
from Student import Student
from Subject import Subject

# Створюємо тестові об'єкти для перевірки класу Lesson
subject1 = Subject("Sport", "necessarily")
teacher1 = Teacher("Yagon", "Don", 32, "Sport")
student1 = Student("Ivan", "Petrenko", 14, "Football")


# Клас Lesson - це урок, який складається з предмета, вчителя та студента
class Lesson:

    # Конструктор - створює новий урок з предметом, вчителем та студентом
    def __init__(self, subject, teacher, student):
        self.subject = subject  # предмет уроку
        self.teacher = teacher  # вчитель, який веде урок
        self.student = student  # студент, який відвідує урок

    # Метод __str__ - повертає коротке текстове представлення уроку (предмет + прізвище вчителя)
    def __str__(self):
        return f"{self.subject.name}, {self.teacher.last_name}"

    # Метод info - повертає детальну інформацію про урок (предмет, вчитель, студент)
    def info(self):
        return (f"Урок: {self.subject.name}, "
                f"викладач: {self.teacher.first_name} {self.teacher.last_name}, "
                f"учень: {self.student.first_name} {self.student.last_name}")

# Коментований код - приклади використання класу Lesson (розкоментуй для перевірки)
# print("First lesson:")
# lesson1 = Lesson(subject1, teacher1, student1)
#
# print(lesson1)
# print(lesson1.info())
#
