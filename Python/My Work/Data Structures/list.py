# it is mutable 
# slicing is possible. Same as string 

# list = []
# for i in range(0,3):
#     list.append(input("Enter name of movie: "))

# print(list)

# WAP to check if a list contains a pellindronme of elements
list2 = [1,2,3,2,1]
list3 = list2.copy()
list3.reverse()
if list3==list2:
    print("The list is pellindrome")
else:
    print("Try again")
