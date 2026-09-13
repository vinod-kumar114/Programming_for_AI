# it means many forms. It allows the same method name to perform different actions depending on the object that calls it. 

# In Python, polymorphism can commonly be achieved through method overriding, where different child classes provide their own implementation of the same method.


# ==== Method Overriding ====

# Method overriding occurs when a child class provides its own implementation of a method that is already defined in its parent class
# It allows a child class to change or customize the behavior inherited from the parent class.



class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

class Cow(Animal):
    def sound(self):
        print("Cow moos")


# Creating objects
dog = Dog()
cat = Cat()
cow = Cow()

# Same method, different behavior
dog.sound()
cat.sound()
cow.sound()