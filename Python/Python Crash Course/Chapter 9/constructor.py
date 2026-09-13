# A constructor is a special method that is automatically executed when an object is created. In Python, the constructor is written as __init__(). It is commonly used to initialize object attributes.

class Student:
    def __init__(self,name,roll):   # constructor
        self.name=name
        self.roll=roll

