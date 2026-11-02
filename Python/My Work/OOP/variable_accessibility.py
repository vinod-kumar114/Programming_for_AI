# Variables based on accessibility

# 1. Public:
    # - accessed directly from inside and outside the class
    # - variables without any underscore are considered public

# 2. Protected:
    # - written with single underscore ( _ ) before its name
    # - accessed within class and sub-classes

# 3. Private:
    # - written with double underscores ( _ _ ) before its name
    # - accessed within class only

# Note: we use getters and setters to access nd modify values of private and protected variables


class Student:
    def __init__(self):
        self.name = "Ali"          # Public variable
        self._marks = 85           # Protected variable
        self.__password = "12345"  # Private variable

    def display(self):
        print("Name:", self.name)
        print("Marks:", self._marks)
        print("Password:", self.__password)

    def getPassword(self):
        return self.__password

s1 = Student()
# s1.display()

print(s1.name)  # accessible
print(s1._marks)
# print(s1.__password)    # inaccessible
# for this we use getPassword method
print(s1.getPassword())  # accessed