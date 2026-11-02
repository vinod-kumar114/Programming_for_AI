# class Person:
#     def __init__ (self, name, age):
#         self.name = name 
#         self.age = age

#     def display_person(self):
#         print("Name: ",self.name, "\nAge: ",self.age)

# class Student(Person):
#     def __init__ (self, name, age, roll_no):
#         self.roll_no = roll_no
#         super().__init__(name, age)


#     def display_student(self):
#         super().display_person()
#         print("Roll no: ", self.roll_no)

# s1 = Student("Ali",16, 102)
# s1.display_student()

# s1.display_person()


class Vehicle:
    def __init__(self, brand):
        self.brand = brand


class Car(Vehicle):
    def __init__(self, brand,doors):
        super().__init__(brand)
        self.doors = doors