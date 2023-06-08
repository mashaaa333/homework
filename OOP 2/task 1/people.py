from base import Person
from Student import Student

person_1 = Person("Hakob", "5")
person_2 = Person("Anahit", "28")
student_1 = Student("Anna", "19", "A")
student_2 = Student("Aram", "21", "B")

Person.display(person_1)
Person.display(person_2)
Student.display_student(student_2)
