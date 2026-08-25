num = int(input("How many numbers do u want: "))
list = []
for i in range(num):
    list.append(int(input(f"Enter num{i+1}: ")))

largest=list[0]
for i in list:
    if i>largest:
        largest=i

print(f"The largest number in the provided list is {largest}")