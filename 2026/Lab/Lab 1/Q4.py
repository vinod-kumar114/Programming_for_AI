# Write a program that takes a list of numbers as input and returns the sum of all the elements in the list.

n = int(input("How many numbers do you want in the list: "))
lis=[]
for i in range(n):
    lis.append(int(input(f"Enter num{i+1}: ")))
    lis[i]

sum=0
for i in lis:
    sum+=i

print("The sum of the provided list is: ",sum)