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
