import csv 
import os.path
from classes.person import Person

class Student(Person):

    def __init__(self, name, age, password, role, school_id):
        super().__init__(name, age, password, role)
        self.school_id = school_id

    def __str__(self):
        return f'\n{self.name.upper()}\n---------------\nage: {self.age}\nid: {self.school_id}\n'

    @classmethod
    def objects(cls):
        students = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")

        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                students.append(Student(**dict(row)))

        return students

# name,age,role,school_id,password
# Lisa,25,Student,13345,xx 
# Jessie,25,Student,12335,xx
# Slater,25,Student,12645,xx
# kim,31,Student,34456,xx
# dave,77,Student,788908,xx
# doug,88,Student,0809890,xx
