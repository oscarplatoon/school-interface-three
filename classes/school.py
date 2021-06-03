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
    
    def add_student(self, student):
        new_student = Student(student['name'], student['age'], student['password'], student['role'], student['id'])
        self.students.append(new_student)
        
        self.write_students_to_csv()
    
    def remove_student(self, student_id):
        
        for i, student in enumerate(self.students):
            if (student.school_id == student_id):
                self.students.pop(i)

        self.write_students_to_csv()

    def write_students_to_csv(self):  

        with open(path, mode='w') as csv_file:
            fieldnames = ['name','age','role','school_id','password']
            student_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            student_writer.writeheader()
            for stud in self.students:
                student_writer.writerow({
                    'name': stud.name, 
                    'age': stud.age, 
                    'role': stud.role, 
                    'school_id': stud.school_id, 
                    'password': stud.password})   