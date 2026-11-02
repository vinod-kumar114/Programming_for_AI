import json
import os

class Student:
    def __init__(self, filename):
        self.filename=filename

    def addStudent(self, name, roll, marks):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                students = json.load(f)
        else:
            students = []

        std = {
            "name": name,
            "roll":roll,
            "marks":marks
        }

        students.append(std)

        with open(self.filename, "w") as f:
            json.dump(students,f,indent=4) 

    def display(self):
        with open(self.filename, "r") as f:
            students = json.load(f)

        for std in students:
            print(f'Name : {std["name"]}, roll: {std["roll"]}, marks: {std["marks"]}')

obj = Student("students.json")

obj.addStudent("Ali", 101, 85)
obj.addStudent("Sara", 102, 90)

obj.display()