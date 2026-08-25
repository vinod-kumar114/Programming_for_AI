# List : ordered, changeable, allows duplicates, can store multiple data types

z = [12, 13, 12, 12, 16, 5.6, True, print()]

# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# print(fruits[-1])

# Built-in common methods
# 1. append() : to add an element in the list
# 2. remove() : to remove an element from the list
# 3. sort() : to sort an element
# 4. pop() 


# # Append

# fruits = ["apple", "banana", "cherry"]
# fruits.append("Gauva")
# print(fruits)


# # remove

# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")
# print(fruits)


# #  update list

# list = ["Ap", "Python", 2002, 114]
# print(list[2])
# list[2] = 66
# print(f"Updated list: ", list)


# # Delete list

# list = ["Ap", "Python", 2002, 114]
# del list[0]
# print(list)


# ===== SHARIAYNS =======


#  LIST TRAVERSING AND METHODS

#  list traversing is also similar to string traversing it can be looped using the index values and directly

# # 1st way: using index
# z = [12, 13, 12, 12, 16, 5.6]
# for i in range(len(z)):
#     print(z[i])

# # 2nd way: directlty on values
# for i in z:
#     print(i)

# ==== Methods
# these are like functions, but they are called with the help of (.) dot

# print(dir(list)) : 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort

# help(list)

"""
 append(self,    object, /)                                                                  
 |      Append object to the end of the list.                                                
 |                                                                                           
 |  clear(self, /)                                                                           
 |      Remove all items from list.                                                          
 |                                                                                           
 |  copy(self, /)                                                                            
 |      Return a shallow copy of the list.                                                   
 |                                                                                           
 |  count(self, value, /)                                                                    
 |      Return number of occurrences of value.                                               
 |                                                                                           
 |  extend(self, iterable, /)                                                                
 |      Extend list by appending elements from the iterable.                                 
 |                                                                                           
 |  index(self, value, start=0, stop=9223372036854775807, /)                                 
 |      Return first index of value.                                                         
 |                                                                                           
 |      Raises ValueError if the value is not present.                                       
 |                                                                                           
 |  insert(self, index, object, /)                                                           
 |      Insert object before index.                                                          
 |                                                                                           
 |  pop(self, index=-1, /)                                                                   
 |      Remove and return item at index (default last).                                      
 |                                                                                           
 |      Raises IndexError if list is empty or index is out of range.                         
 |                                                                                           
 |  remove(self, value, /)                                                                   
 |      Remove first occurrence of value.                                                    
 |                                                                                           
 |      Raises ValueError if the value is not present.                                       
 |                                                                                           
 |  reverse(self, /)                                                                         
 |      Reverse *IN PLACE*
"""

l=[1,2,3,4,5,6]

l.append(7) # 7 is the value at the last index
l.insert(7,8) # here 7 is the inex, an 8 is the value
l.extend([9,10,11,12]) # last m multiple values ko add krny m help krta hy
l.remove(6) # removes the 1st most same number

# p = l.pop(3) # removes the number at index 3 and stores somewhere in the memory
# print(p)

# index = l.index(7) # ye 7 ki index batata hy ke 7 kaha pr hy
# print(index)

# count = l.count(2) # 2 ko list m count krta hy ke kitni bar aaya hy
# print(count)

# l.sort() # list ko ascending order m sort out krta hy

# l.reverse() # list ko reverse krta hy
# print(l)

# copy = l.copy() # list ki aik copy banata hy
# print(copy)

# copy.clear() # list ke sabhi elements ko clear ya remove kr deta hy
# print(copy)

# l[0]=100 # it can easily change the value at index 0
# print(l)


# # q1: Print positive and negative elements of an List
# l=[1,2,-3,4,5,-6,-7,8,9-10]
# print("Positive elemets are: ")
# for i in l:
#     if i>=0:
#         print(i, end=', ')
# print('\nNegative elements are: ')        
# for i in l:
#     if i<0:
#         print(i, end=', ')


# # q2: Mean of List elements
# l=[1,2,3,4,5,6,7,8]
# sum=0
# for i in l:
#     sum+=i
# mean = sum/len(l)
# print(mean)


# # q3: Find the greatest element and print its index too
# l=[12,36,14,19,127,6,8]
# g = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i]>g:
#         g=l[i]
#         index = i   
# print(g,"at index" ,index, "is the greatest number")


# # q4: Find the second greatest element
# l=[12,36,14,19,127,70,6,8]
# g = l[0]
# sec_g= 0
# for i in range(len(l)):
#     if l[i]>g:
#         sec_g=g
#         g=l[i]
#     elif l[i]>sec_g:
#         sec_g=l[i]
# # yaha pr hamne ye kiiya hy ke hum largest value g m store krny se pehly g ko sec_g m assign kr rhy hen. Is se ye ho raha hy ke hum second largest ko bhi store kr rhy hen. Ab aik issue ye tha ke agar list m largest ke baad koee sec large value aati to usky liye 1st wli if statement kaam ni krti, us liye hamne elif m condition lagai ke wo puri list m dekhy ke koee dusra sec large to element ni hy.
# print(sec_g,"is the second greatest number")


# # q5: Check if List is sorted or not
# l = [12,36,40,127]
# s=True
# for i in range(len(l)-1):
#     if l[i]>l[i+1]:
#         s=False
#         break # Agay check karne ki zaroorat nahi, loop yahin rok dein

# if not s:
#     print("The list is not sorted")
# else:
#     print("The is list is sorted")







# Q: Write a program to take a list and a number input from user and then delete all elements in the list less than that number.


number = int(input("enter the number: "))

nums = int(input("How many numbers do u want in the list: "))
list = []
for i in range(nums):
    list.append(int(input(f"Enter num{i+1}: ")))

print("Provided list: ", list, end=" ")

newlist=[]
for i in list:
    if i>=number:
        newlist.append(i)

print("\nReduced list: ", newlist, end=" ")


"""
Ek Short Tip (List Comprehension)Aap apne is newlist wale poore loop ko sirf aik line mein likh sakte hain. Isay Python mein list comprehension kehte hain aur ye bohot fast hoti hy:

# Is aik line se aap ka poora loop replace ho sakta hy
newlist = [i for i in my_list if i >= number]

"""