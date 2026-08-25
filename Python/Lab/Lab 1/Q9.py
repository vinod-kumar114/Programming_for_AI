# Write a Python program to create the multiplication table (from 1 to 10) of a number.


num = int(input("Enter a number: "))

n=1
for i in range(num, num*10+1, num):
    print(f"{num} * {n} = {i}")
    n+=1