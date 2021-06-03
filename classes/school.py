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

    def add_student(self,student_data):
        self.students.append(Student(**student_data))
        self.save()

    def delete_student(self,id):
        for student in self.students:
            if id == student.school_id:
                self.students.remove(student)
        self.save()

    def save(self):
        output = []
        for student in self.students:
            output.append([student.name,student.age,student.role,student.school_id,student.password])
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path,'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['name','age','role','school_id','password'])
            csvwriter.writerows(output)

        

# name,age,role,school_id,password
# Lisa,25,Student,13345,xx 
# Jessie,25,Student,12335,xx
# Slater,25,Student,12645,xx
# kim,31,Student,34456,xx
# dave,77,Student,788908,xx
# doug,88,Student,0809890,xx

