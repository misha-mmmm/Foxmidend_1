from Teacher import Teacher
from Student import Student
from Subject import Subject

subject1 = Subject("Sport", "necessarily")
teacher1 = Teacher("Yagon", "Don", 32, "Sport")
student1 = Student("Ivan", "Petrenko", 14, "Football")


class Lesson:

    def __init__(self, subject, teacher, student):
        self.subject = subject
        self.teacher = teacher
        self.student = student

    def __str__(self):
        return f"{self.subject.name}, {self.teacher.last_name}"

    def info(self):
        return (f"Урок: {self.subject.name}, "
                f"викладач: {self.teacher.first_name} {self.teacher.last_name}, "
                f"учень: {self.student.first_name} {self.student.last_name}")

#
# print("First lesson:")
# lesson1 = Lesson(subject1, teacher1, student1)
#
# print(lesson1)
# print(lesson1.info())
#
