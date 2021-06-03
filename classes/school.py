from classes.staff import Staff
from classes.student import Student
import os.path
import csv


class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self, student_data):
        new_student = Student(**dict(student_data))
        self.students.append(new_student)
        self.store_students()

    def store_students(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/updated_students.csv")
        with open(path, 'w', newline = '\n') as csvfile:
            field_names = ['name', 'age', 'password', 'role', 'school_id']
            writer = csv.DictWriter(csvfile, field_names)
            writer.writeheader()
            for student in self.students:
                writer.writerow({
                    'name': student.name,
                    'age': student.age,
                    'role': student.role,
                    'school_id': student.school_id,
                    'password': student.password})

    def delete_student(self, student_id):
        self.students.remove(self.find_student_by_id(student_id))
        self.store_students()

        # my_path = os.path.abspath(os.path.dirname(__file__))
        # path = os.path.join(my_path, "../data/updated_students.csv")
