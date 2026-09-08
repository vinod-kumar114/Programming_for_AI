"""Given a list of integers, find the element that appears more than n/2 times, where n is the total 
number of elements in the list. 
You may assume that a majority element always exists. 
1. Create a function named majority_element(nums).
2. Count the frequency of each element.  
3. Store the frequencies using a dictionary.  
4. Return the element whose frequency is greater than n/2. """



def majority_element(nums):
    dic = {}
    for i in nums:
        dic[i]=dic.get(i,0)+1
    
    for key, value in dic.items():
        if value > len(nums)//2 :
            print(key)

num = [3, 2, 3, 4, 3, 3, 1]

majority_element(num)