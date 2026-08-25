# Write a program to take an integer list input from user and count all the even numbers in that list and print the count.

count = 0
n = int(input("How many numbers do you want in the list: "))
lis=[]
for i in range(n):
    lis.append(int(input("Enter num: ")))
    lis[i]

for num in lis:     # yaha num index ni, original value ko point kr raha hy
    if num%2==0:
        count+=1

print("Total even numbers in the list are ",count)