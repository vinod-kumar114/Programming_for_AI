""" Given a list of integers, determine whether any value appears more than once in the list. 
Return True if at least one duplicate exists; otherwise return False. 
1. Create a function named contains_duplicate(nums).  
2. Use a set to keep track of values that have already been encountered.  
3. If a value is already present in the set, identify it as a duplicate. """



def contains_duplicate(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)   
    return False


lis = [1,2,3,4,5,3,3,4,5,5,2,4,3]
lis2 = [1,2,3,4,5]
print(contains_duplicate(lis))   

