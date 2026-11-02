"""In OOP u write classes to represent real world things and situations, and objects based on these classes. 
=> Making an object from class is called instantiation, and u work with instances of a class.
"""

# Creating a Dog class
# DOg class will store a name, and an age, and we'll give each dog the ability to sit() and roll_over():

class Dog():
    def __init__ (self,name,age):   #=> __init__() is the constructor in python
        self.name=name
        self.age=age
    
    def sit(self):
        print(self.name.title()+" is sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over.")

dog1 = Dog("Tommy",3)

dog1.sit()
dog1.roll_over()



"""
=> A function that's part of a class is a method.
=> __init__() is the constructor in python

We define the __init__() method to have three parameters: self, name and age. The self parameter is required in the method definition, and it must come first before the other parameters. It must be included in the definition because when Python calls this __init__() method later (to create an instance of Dog), the method call will automatically pass the self argument. 
Every method call associated with a class automatically passes self, which is a reference to the instance itself; it gives the individual instance access to the attributes and methods in the class. When we make an instance of Dog, Python will call the __init__() method from the Dog class. We'll pass Dog() a name and an age as arguments; self is passed automatically, so we don't need to pass it. Whenever we want to make an instance from the Dog class, we'll provide values for only the last two parameters, name and age.


============== self ===========
- Jo object create hue hy usko refer krta hy self
- ye python ko specify krta hy ke mujhy kis object ke liye ye variables and methods use krty hen
- represents the instance of the class that is currently being created or operated on.

- jab hum koee bhi new object banaty hen to python bs us object ke liye memory assign krti hy, na ke whole class ke liye. And self ko use krky yahi milta hy.

- self does the same thing that 'this pointer' does
- self in Python == this in C++. Both point to the current object.

"""

