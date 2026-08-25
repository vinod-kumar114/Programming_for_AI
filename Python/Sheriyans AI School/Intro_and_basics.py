# Python is an interpreted language.

# Line by line run kregi. Then usy execute kregi


print("Namaste, I am learning Python")


# Comments are given by (hashtag: #)
# to comment all, we can use a ( "Doc String": """  This is Multiline    """ )
"""shjfbsdjbjbsdjbjsdbbdjv n vjhbdsnd fjhuhdgfhsdjfabsjhdfag  vmnbvn bvbsdbd jdksnf nknisdn  fbdsyrywb"""

# to comment all use: ctrl+/

"""

# Variables: these are like containers, where we store some sort of values or data
# Rule: Don't use space before the varible
Name = "Vinod"

# In python, we don't need to add any datatype before the variable. But to find what type of data is stored in the variable, we can use: print(type(Name))

print(type(Name))

# For storing complex number, add j after it

a = 15j
print(type(a))


a = "A"
b = "😂"
# we can get its unique code using: print(ord(a))
print(ord(b))

# we can convert from unique code to character, using print(chr(65)). Example: Unique code of A is 65
print(chr(65))  # answer is A

# we can also use a complete string and find its number, using indexing which starts with 0, also with -1: print(name[0])

name= 'Vinod' # here index of v is 0, i=1, n=2, o=3, d=4
print(name[0], name[-5])

# String Slicing











# Type Conversion Functions:

# 1. Explicit
# int(), float(), str(), bool()
x=24
x = str(x)
print(type(x))

z="12"
z=int(z)
print(type(z))



# 2. Implicit: jo python khud convert deti hy, for example: 
print(12/3) # answer is 4.0, not 4



# Output: it is shown using only and only "print()" finction

# name="Vinod"
# age=18

# print("My name is", name, "and my age is", age, "years.")

# # Formatted string: add f before starting the line
# print(f"My name is {name} and my age is {age} years.")

# Input: it is taken using the "input()" function.default data type of input is always string reason is simple you can store anything in string. We have to manually convert the input for the other datatypes.

name = input("Hello, what is your name: ")


# if mujhy integer datatype ka nput lena hy to me aisy kroonga

age = int(input("What is your age: "))

print(type(age))

print("My name is", name)
print("I am",age, "years old")

"""
# Operators:
# 1. Arithmetic: +, -, *, /, // (flow division), ** (exponent or power), % (mod, used for reminder)
# 2. Assignment: =, +=, -=, *=, /=, %=,  ...
# 3. Comparison: ==, !=, >, <, >=, <=     /// They will always provide a boolean answer: True(1), or False(0)
    # These can be used with strings as well. But they are compared with the help of their ASCII values. Use of print(ord(A))
# 4. Logical Operators: AND, OR, NOT (to reverse the booleanvalue)


# Note: Python follows BODMAS rule





# Flow division is used to give the answer in integer. For example, if the answer is 12.5, with flow division, it will discard the values after dot(.)