"""3.A payment system receives a large collection of transaction IDs. Due to network problems, some transactions may
appear more than once.Develop a solution that identifies duplicate transaction IDs and produces a collection
containing only unique transactions. Requirement: Consider the performance implications when processing
thousands of transaction IDs."""


nums = int(input("No of IDs: "))
lis = []
for i in range(nums):
    lis.append(int(input(f"Enter num{i+1}: ")))

print("Provided list: ", lis, end=" ")

# printing IDs of unique transactions
s = set(lis)
newList=list(s)
print("\nUpdated list: ", newList)