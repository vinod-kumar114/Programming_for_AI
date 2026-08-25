# Write a program to make a simple calculator performing the four basic operations (+, -, *, /) on two numbers input by user. The following conditions must be satisfied:
# a) A ‘+’ sign must not be used for addition.
# b) You can only use a maximum of 3 variables. No more variables are allowed.
# c) Your program should ask the


num1= int(input("Enter num1: "))
num2= int(input("Enter num2: "))

op = input("Choose any operation (+, -, *, /): ")

if op == '+':
    print(num1-(-num2))
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == "/":
    if num2!=0:
        print(num1/num2)
    else:
        print("Can't divide, since num2 is 0")
else:
    print("Invalid Operation")