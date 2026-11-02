# 1. TUPLE CREATION OPERATION
my_tuple = (10, 20, 30, 20, 40)


# 2. SINGLE ELEMENT TUPLE OPERATION (COMMA IS REQUIRED)
single_item = (50,)


# 3. ACCESSING ELEMENTS (INDEXING) OPERATION
first_item = my_tuple[0]


# 4. NEGATIVE INDEXING OPERATION
last_item = my_tuple[-1]


# 5. TUPLE SLICING OPERATION
sub_tuple = my_tuple[1:4]


# 6. COUNT METHOD OPERATION
twenty_count = my_tuple.count(20)


# 7. INDEX METHOD OPERATION
idx_30 = my_tuple.index(30)


# 8. MEMBERSHIP CHECK (IN) OPERATION
is_present = 20 in my_tuple


# 9. TUPLE CONCATENATION (+) OPERATION
combined_tuple = my_tuple + (50, 60)


# 10. TUPLE REPETITION (*) OPERATION
repeated_tuple = (1, 2) * 3


# 11. TUPLE LENGTH (LEN) OPERATION
length = len(my_tuple)


# 12. TUPLE UNPACKING OPERATION
a, b, c, d, e = my_tuple


# 13. TUPLE UNPACKING WITH ASTERISK (*) OPERATION
head, *middle, tail = my_tuple


# 14. MIN, MAX, AND SUM OPERATIONS
min_val = min(my_tuple)
max_val = max(my_tuple)
total_sum = sum(my_tuple)


# 15. SORTED FUNCTION (RETURNS A NEW SORTED LIST)
sorted_list_from_tuple = sorted(my_tuple)


# 16. CONVERTING TUPLE TO LIST (TO MODIFY) AND BACK TO TUPLE
temp_list = list(my_tuple)
temp_list.append(99)
modified_tuple = tuple(temp_list)


# 17. NESTED TUPLE ACCESS OPERATION
nested_tuple = ((1, 2), (3, 4))
nested_val = nested_tuple[1][0]


# 18. DELETING TUPLE (DEL) OPERATION
del my_tuple