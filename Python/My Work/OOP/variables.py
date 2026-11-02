# Instance variables VS Class variables

# 1. Instance variables belong to a specific object. The valule only belongs to that specific object. They are usually defined using self.

# 2. A class variable belongs to the class rather than to a particular object. Its value is shared among all objects of the class.abs

class Student:

    uni = "FAST NUCES"  # class variable

    def __init__(self,name,roll):   # constructor
        self.name=name  # instance
        self.roll=roll

