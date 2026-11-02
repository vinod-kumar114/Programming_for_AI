# mostly used in python
# immutable
# slicing is possible. Same as list


# tup = (1,2,3,4,5,5,5,6)

# # it has only 2 mthods. index, count

# print(tup.index(2)) # it will show where the 2 is available
# print(tup.count(5)) # no of times 5 has occured



tup = ('c', 'a', 'a', 'b', 'b', 'a')
print(tup.count('a'))

lis = list(tup)
lis.sort()
print(lis)