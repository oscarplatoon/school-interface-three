from classes.staff import Staff
from classes.student import Student
import csv
import os

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
        self.student_data = student_data
        self.students.append(Student(**self.student_data))
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['name', 'age', 'password', 'role', 'school_id'])
            writer.writeheader()
            for student in self.students:
                writer.writerow({'name':student.name, 'age':student.age, 'password':student.password, 'role':student.role, 'school_id':student.school_id})
    
    def remove_student(self, student_id):
        self.student_id = student_id
        for student in self.students:
            if student.school_id == self.student_id:
                self.students.remove((student))
                my_path = os.path.abspath(os.path.dirname(__file__))
                path = os.path.join(my_path, "../data/students.csv")
                with open(path, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=['name', 'age', 'password', 'role', 'school_id'])
                    writer.writeheader()
                    for student in self.students:
                        writer.writerow({'name':student.name, 'age':student.age, 'password':student.password, 'role':student.role, 'school_id':student.school_id})

    

