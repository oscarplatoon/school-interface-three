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
            

    def delete_student(self, student_id):
        deleted_id = student_id
        # looping through list of student obj's
        for student in self.students:
        # find the student that needs to be deleted
            if student.school_id == deleted_id:
            # delete student from self.students
                self.students.remove(student)
                # update the student.csv file
        with open(path, mode= 'w') as csvfile:    
            writer = csv.writer(csvfile)
            writer.writerow(['name', 'age', 'role', 'school_id', 'password'])
            for student_obj in self.students:
                writer.writerow([student_obj.name, student_obj.age, student_obj.role, student_obj.school_id, student_obj.password])
                
      

            

        
    #     # with open('first.csv', 'rb') as inp, open('first_edit.csv', 'wb') as out:
    # writer = csv.writer(out)
    # for row in csv.reader(inp):
    #     if row[2] != "0":
    #         writer.writerow(row)