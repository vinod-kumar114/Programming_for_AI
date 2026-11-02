# used to call methods feom parent class in child class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name,age)
        self.roll = roll


    def display(self):
        print(f"{self.name}, {self.age}, {self.roll}")

s1 = Student("ALi", 19, 101)
s1.display()




