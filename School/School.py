
from Lesson import Lesson
from Teacher import Teacher
from Student import Student
from Subject import Subject
class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.lessons = []


    def add_student(self, student):
        self.students.append(student)




    def add_teacher(self, teacher):
        self.teachers.append(teacher)




    def add_lesson(self, lesson):
        self.lessons.append(lesson)



    def print_students(self):
        print(f"Учні вчителя: {self.first_name} {self.last_name} ")
        if not self.students:
            print("No students")
        else:
            for student in self.students:
                print(student.first_name, student.last_name)


student1 = Student("Danya", "Varenik", 16, "Sport")
student2 = Student("Olena", "Shevchenko", 17, "Math")
student3 = Student("Maksym", "Bondarenko", 15, "Swimming lesson")
student4 = Student("Anastasia", "Koval", 16, "Sport")
student5 = Student("Dmytro", "Melnyk", 18, "Math")
student6 = Student("Sofia", "Tkachenko", 15, "Swimming lesson")
student7 = Student("Artem", "Kravchenko", 17, "Sport")


teacher1 = Teacher("Roman", "Vodolaz", 32, "Swimming lesson")
teacher2 = Teacher("Nazar", "Barbos", 36, "Math")
teacher3 = Teacher("Yagon", "Don", 30, "Sport")


subject1 = Subject("Swimming lesson", "necessarily")
subject2 = Subject("Math", "necessarily")
subject3 = Subject("Sport", "necessarily")


teacher1.add_student(student3)
teacher1.add_student(student6)
teacher2.add_student(student2)
teacher2.add_student(student5)
teacher3.add_student(student1)
teacher3.add_student(student4)
teacher3.add_student(student7)

print("First lesson:", subject1.name)
print("Teacher:", teacher1.first_name, teacher1.last_name)
teacher1.print_students()
print()
print("Second lesson:", subject2.name)
print("Teacher:", teacher1.first_name, teacher1.last_name)
teacher2.print_students()
print()
print("Third lesson:", subject3.name)
print("Teacher:", teacher3.first_name, teacher3.last_name)
teacher3.print_students()
print()


