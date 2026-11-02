# import os

# class StudentManager:
#     def __init__(self, filename="students.txt"):
#         self.filename = filename

#     def addStudent(self, name, age):
#         with open(self.filename, "a") as file:
#             file.write(f"{name}, {age}\n")
#             print(f"{name} added")

#     def display(self):
#         # Pehle check karo ke file exist karti hai ya nahi
#         if not os.path.exists(self.filename):
#             print("File not found")
#             return

#         with open(self.filename, "r") as file:
#             std = file.readlines()
#             if not std:
#                 print("File is empty")
#             else:
#                 for l in std:
#                     print(l.strip())

# manager = StudentManager("students.txt")

# # Methods call kiye
# manager.addStudent("Ali", 20)
# manager.addStudent("Ahmed", 21)
# manager.addStudent("Fatima", 19)

# manager.display()

import os

# class StudentM:
#     def __init__(self, filename="student.txt"):
#         self.filename=filename

#     def addStudent(self, name, roll, marks):
#         if not os.path.exists(self.filename):
#             print("File does not exist")
#             return;
#         with open(self.filename,"a") as file:
#             file.write(f"{name}, {roll}, {marks}\n")
#             print("Student added")

#     def display(self):
#         with open(self.filename, "r") as f:
#             for line in f:
#                 name, roll_no, marks = line.strip().split(",")
#                 print(name, roll_no, marks)

# obj = StudentM("students.txt")

# obj.addStudent("Ali", 101, 85)
# obj.addStudent("Sara", 102, 90)

# obj.display()


class StudentManager:
    def __init__(self, filename):
        self.filename = filename

    def add_student(self, name, roll_no, marks):
        with open(self.filename, "a") as f:
            f.write(f"{name},{roll_no},{marks}\n")

    def display_students(self):
        with open(self.filename, "r") as f:
            for line in f:
                name, roll_no, marks = line.strip().split(",")
                print(name, roll_no, marks)


obj = StudentManager("students.txt")

obj.add_student("Ali", 101, 85)
obj.add_student("Sara", 102, 90)

obj.display_students()