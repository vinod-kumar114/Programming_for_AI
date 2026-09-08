"""Given a list of integers and an integer k, find the k elements that occur most frequently in the list. 
1. Create a function named top_k_frequent(nums, k).  
2. Count the frequency of each element using a dictionary.  
3. Rank the elements according to their frequency.  
4. Return the k most frequent elements.  
5. Use sorted() and a lambda expression for ranking. """

def top_k_frequent(nums, k):
    dic ={}
    for num in nums:
        dic[num]=dic.get(num,0)+1
    
    rank=sorted(dic.items(), key=lambda num: num[0], reverse=True)
    for (i,j) in rank[:k]:
        print(i)

num = [1, 2, 3, 4, 5, 3, 3, 4, 5, 5, 2, 4, 3]

top_k_frequent(num,3)