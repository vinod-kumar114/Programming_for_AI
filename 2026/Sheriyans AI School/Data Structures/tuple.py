"""
Tuple:
=> can't change it
=> duplicates alllowed
=> ordered
=> can contain different type of data


we use paranthesis


tuple have two methods:

a.index()
a.count()

"""

# a=(1,2,3,4,4,4,5,5,6,7, print(), "hello")

# print(a)

# index=a.index(5)
# print(index)

# count = a.count(4)
# print(count)

# Tuples are traversed in the same manner as List are traversed
# for i in range(len(a)):
#     print(a[i])




#  ===== There is no difference in LIST and TUPLE except changeability
# List can be changed, and tuple can't be changed
# kind of a string


# ===== Tuple Unpacking
a,b,c,d=(1,2,3,4) # here a=1, b=2, c=3, d=4
print(d)

a=(3) # ye int data type show krega, q ki isme ye unpack krky show kr raha hy
print(type(a))
# if hum chahty hen k ye tuple me show kry to hum aisy kr sakty hen
a=(3,)
print(type(a))