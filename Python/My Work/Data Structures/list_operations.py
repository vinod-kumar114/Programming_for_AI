# 1. APPEND OPERATION
nums = [10, 20]
nums.append(30)


# 2. INSERT OPERATION
nums.insert(1, 15)


# 3. EXTEND OPERATION
nums.extend([40, 50])


# 4. DELETE (DEL) OPERATION
del nums[0]


# 5. POP OPERATION
popped_val = nums.pop()


# 6. REMOVE OPERATION
nums.remove(15)


# 7. UPDATE OPERATION
nums[0] = 99


# 8. SEARCH (IN) OPERATION
is_present = 99 in nums


# 9. INDEX OPERATION
idx = nums.index(40)


# 10. COUNT OPERATION
cnt = nums.count(99)


# 11. SORT OPERATION
nums.sort()


# 12. SORTED FUNCTION
sorted_nums = sorted(nums, reverse=True)


# 13. REVERSE OPERATION
nums.reverse()


# 14. SLICING OPERATION
sub_list = nums[0:2]


# 15. CONCATENATION OPERATION
combined = nums + [100, 200]


# 16. REPETITION OPERATION
repeated = [0] * 4


# 17. COPY OPERATION
nums_copy = nums.copy()


# 18. CLEAR OPERATION
nums.clear()



numbers = [10, 20, 5, 30, 15]

for index, item in enumerate(numbers):
    print(index, item)
# Prints elements with their index using enumerate()




matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Outer loop rows ke liye, inner loop columns ke liye
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # Nayi row ke liye newline