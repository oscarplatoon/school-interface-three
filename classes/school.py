from classes.staff import Staff
from classes.student import Student
import os.path
import csv
my_path = os.path.abspath(os.path.dirname(__file__))

path = os.path.join(my_path, "../data/students.csv")


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
        
        with open(path, mode = 'a') as csvfile:
            student_writer = csv.DictWriter(csvfile, fieldnames=['name','age','role', 'school_id', 'password'])
            student_writer.writerow(student_data)
            self.students.append(Student(**student_data))
            
            
        
        