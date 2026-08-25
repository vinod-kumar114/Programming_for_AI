
# Range Function: it is used to genrate a sequence of numbers. Syntax: range(start, stop, steps)
# you have 3 points from where you want to start, till where you want to stop and how many steps you want.
# If you don’t mention start point the default value will be 0. If you don’t mention the steps the default steps will be 1.you have to mention the stop point otherwise the range function will not work.

#  Range function is used in for loop


# For Loop

#fruits = ["apple", "banana", 'cherry']
#for i in fruits:
#    print(i) # har value ko alag alag new line pr print krega. isme hum index ka use ni kr rahy. jab hum range fun use krty hen to phir index ka use hota hy.

#for i in range(len(fruits)):
#    print(fruits[i]) # yaha hum index ko access krky unhy print krwa rhy hen, best method hy agar kabhi hamen indexing ki need ho to. Like agar hamen list ko index ki help se modify krna pry to



# a = range(1, 21, 1) # here we have put stop point 21 cuz it will check if the next num is 21, it will stop at 20.

# for i in a:
#     print(i)

# for i in range(11): # only stop is given, other values are default
#     print(i)

# #  16 to 1
# for i in range(16, 0, -1):
#     print(i)

# # -3 to -15
# for i in range(-3, -16, -1):
#     print(i)

# Print a table of 5
# for i in range(5, 51, 5):
#     print(i)


# # Take input from the user and create a table
# num = int(input("Enter the number: "))
# for i in range(num, num*10+1, num):
#     print(i)


# // For Loop for Strings

# 1st way

# a = "FAST"
# print(a[0], a[1], a[2], a[3]) # instead of doing this, we can use range fun
# for i in range(4):
#     print(a[i])    # What if we don't know how many characters are there such as: I study in FAST. yaha hum characters ko count krty to ni rahengy na. 
# For this we can use "len()" function

# print(len(a))

# b = "I study in FAST"
# #print(len(b)) # 15 length
# # Look, string ki index start hoti hy 0 se, string ki lenth start hoti hy 1 se. So lentgh hamesha last index se aik ziyada ayegi, aur dekha jaye to range fun m default start point 0 hy and stop point +1 hy. yah range m len fun achhy se kaam krega.
# for i in range(len(b)):
#     print(b[i])


#2nd Way: Iterating directly over the string

# a = "Vinod is intelligent"
# for i in a:
#     print(i)

# break statement
# for i in range(1,21):
#     if i==16:
#         break
#     else:
#         print(i)

# Continue statement # Ye loop ko redirect krta hy, means ke jis condition pr continue laga hua hy usky neechy wali cheezen kaam ni krengi
# for i in range(1,21):
#     if i==16:           # 16 print ni hua, q ki isme aisa hua ke jaisy hi i==16 hua to usky neechy continue tha, to continue ki neechy wli print function ne kaam ni kiiya... Step ko miss krna hy 
#         continue
#     print(i)

# # else statement: works with break, agar break chala to else ni chalga, and if break ni chala to else chalega
# for i in range(1,21):
#     if i==16:
#         print("Break statement executed") # jaisy hi 16 pr aya to break ne kaam kiiya, aur statement execute ho gyee
#         break
#     print(i)
    
# else: # else bs aik contition pr ni chal raha, baki sab pr chal raha hy
#         print("Break statement did not execute")

# Questions

# # q1
# num = int(input("Enter a number: "))
# for i in range(num):
#     print("Hello World")

# # q2
# num = int(input("Enter a number: "))
# for i in range(num):
#     print(i+1)

# # q3
# num = int(input("Enter a number: "))
# for i in range(num, 0, -1):
#     print(i)

# # q4
# num = int(input("Enter a number: "))
# for i in range(num, num*10+1, num):
#     print(i)

# # q5
# n=0
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     n=n+i
# print(n)

# # q6: Factorial of a number
# n=1
# num = int(input("Enter a number: "))
# for i in range(1,num+1):
#     n=n*i
# print(n)

# # q7
# even=0
# odd=0
# start = int(input("Enter the starting num: "))
# end = int(input("Enter the ending num: "))
# for i in range(start,end+1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# print(f"Even: {even} \nOdd: {odd}")


# # q8: factors of a num
# num = int(input("Enter a number: "))
# for i in range(1,num):
#     if num%i==0:
#         print(i)


# # q9
# sum=0
# num = int(input("Enter a number: "))
# for i in range(1,num):
#     if num%i==0:
#         sum+=i
# if sum==num:
#     print(f"{num} is a Perfect number")
# else:
#     print(f"{num} is not a Perfect number")


# # q10
# num = int(input("Enter a number: "))
# p=1
# for i in range(2,num):
#     if num%i==0:
#         p=0
#         break
# if p==1:
#     print(f"The {num} is a Prime")
# else:
#     print(f"The {num} is not a prime")


# #  11
# strin = input("Enter the string: ")
# reve = ""
# for i in range(len(strin)-1, -1, -1):
#     reve+=strin[i]
# print(reve)
# # Yaha sab -1 q hen. Isky 3 reaon: 1. len(strin)-1 , isko is liye -1 hy q ki hamari length jo hy wo index+1 aati hy (index se aik ziyada), so index ko mantain rakhny ke liye -1 kiiya. 2. -1 is liye hy q ki hamen stop position hamesha +1 krni hoti hy, yaha pr hum peechhy ja rhy hen na, so 0 ke aik peechhy -1 hota hy. is se ye hoga ka hamara 0th index wla bhi element prit hoga. 3. -1 is liye q ki ham peechhy ja rhy hen na 


# q12
# a = input("Enter a string: ")
# full = len(a)
# half=len(a)//2
# #print(half)
# b=''
# for i in range(half):
#     b=b+a[i]
# c=''
# for i in range(full-1,half,-1):
#     c=c+a[i]

# if b==c:
#     print("The string is a pellindrome")
# else:
#     print("The string is not a pellindrome")

#  Another way:
# hamari pass reversed string hy, so agar origal and reversed ko check kren ke equal hy to bs pellindrome mil jayega.

# a = input("Enter the string: ")
# b = ""
# for i in range(len(a)-1, -1, -1):
#     b+=a[i]

# if b==a:
#     print("The string is a pellindrome")
# else:
#     print("The string is not a pellindrome")


# #  Efficient way:
# a = input("Enter a string: ")

# # String ko reverse kar ke compare karein
# if a == a[::-1]:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")



# # q13
# x = "jnjhwuey826330294ui&&^%&*@*(@i8)"
# char = 0
# dig=0
# spchr =0

# for i in x:
#     if i.isalpha():
#         char+=1
#     elif i.isdigit():
#         dig+=1
#     else:
#         spchr+=1

# print(f"Digits: {dig} , Characters: {char}, Special characters: {spchr}")

















#  ========= While Loop ========
# depends on a condition. Jab tak condition true hy, while loop kaam krta rahega, jaisy hi condition false hogi, while loop end.

# a=1
# while a<=10:
#     print(a)
#     a+=1


#  



# # q2
num = 256 # int(input("Enter a number: "))
while num>0:
    ld=num%10
    print(ld, end='')
    num=num//10



 