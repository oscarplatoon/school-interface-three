import csv
import os.path
        
from classes.staff import Staff
from classes.student import Student

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
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        self.students.append(Student(**dict(student_data)))

        with open(path, mode = 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['role', 'name', 'age', 'school_id', 'password'])
            writer.writeheader()

            for student in self.students:
                name = student.name
                age = student.age
                role = student.role
                id = student.school_id
                pw = student.password
                writer.writerow({'name': name,'age': age, 'role': role, 'school_id': id, 'password': pw})

 
    def delete_student(self, delete_student_id):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path, mode = 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['role', 'name', 'age', 'school_id', 'password'])
            writer.writeheader()

            for student in self.students:
                
                name = student.name
                age = student.age
                role = student.role
                id = student.school_id
                pw = student.password
                if id == delete_student_id:
                    pass
                elif id != delete_student_id:
                    writer.writerow({'name': name,'age': age, 'role': role, 'school_id': id, 'password': pw})
        
        self.students = Student.objects()
        



                