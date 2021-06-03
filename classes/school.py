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

    #add_student method
    def add_student(self, student_data):
        self.student_data = student_data
        print(self.student_data)

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path, mode='a') as csvfile:
            fieldnames = ['name', 'age', 'role', 'school_id', 'password']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(self.student_data)
            
    
    def delete_student(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                self.students.remove(student)
                break

        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path, mode ="w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'age', 'role', 'school_id', 'password'])
            for student in self.students:
                writer.writerow([student.name, student.age, student.role, student.school_id, student.password])
