# 1. SET CREATION OPERATION (DUPLICATES AUTOMATICALLY REMOVED)
my_set = {10, 20, 30, 40, 20}


# 2. EMPTY SET CREATION (MUST USE set(), NOT {})
empty_set = set()


# 3. ADD ELEMENT OPERATION
my_set.add(50)


# 4. UPDATE OPERATION (ADD MULTIPLE ELEMENTS / ITERABLES)
my_set.update([60, 70, 80])


# 5. REMOVE OPERATION (RAISES KEYERROR IF ELEMENT NOT FOUND)
my_set.remove(80)


# 6. DISCARD OPERATION (NO ERROR IF ELEMENT NOT FOUND)
my_set.discard(99)


# 7. POP OPERATION (REMOVES AND RETURNS AN RANDOM/ARBITRARY ELEMENT)
popped_val = my_set.pop()


# 8. MEMBERSHIP CHECK (IN / NOT IN) OPERATION
is_present = 30 in my_set


# 9. UNION OPERATION (COMBINES ELEMENTS FROM BOTH SETS)
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)  # Alternative: set_a | set_b


# 10. INTERSECTION OPERATION (COMMON ELEMENTS ONLY)
intersection_set = set_a.intersection(set_b)  # Alternative: set_a & set_b


# 11. DIFFERENCE OPERATION (ELEMENTS IN SET_A BUT NOT IN SET_B)
diff_set = set_a.difference(set_b)  # Alternative: set_a - set_b


# 12. SYMMETRIC DIFFERENCE OPERATION (ELEMENTS IN EITHER SET, BUT NOT BOTH)
sym_diff_set = set_a.symmetric_difference(set_b)  # Alternative: set_a ^ set_b


# 13. SUBSET CHECK (ISSUBSET) OPERATION
is_sub = {1, 2}.issubset(set_a)  # Alternative: {1, 2} <= set_a


# 14. SUPERSET CHECK (ISSUPERSET) OPERATION
is_super = set_a.issuperset({1, 2})  # Alternative: set_a >= {1, 2}


# 15. DISJOINT CHECK (ISDISJOINT - NO COMMON ELEMENTS)
is_disjoint = {10, 20}.isdisjoint({30, 40})


# 16. SET COPY OPERATION
set_copy = my_set.copy()


# 17. SET COMPREHENSION OPERATION
even_squares = {x**2 for x in range(10) if x % 2 == 0}


# 18. CLEAR OPERATION (REMOVES ALL ELEMENTS)
my_set.clear()


# 19. DELETING SET (DEL) OPERATION
del my_set