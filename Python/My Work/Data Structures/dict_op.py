keys = ['name', 'age', 'grade']

new_student = dict.fromkeys(keys, 'Unknown')
print(new_student)


item_list = list(new_student)
print(item_list)





# 1. DICTIONARY CREATION
my_dict = {"name": "Alice", "age": 25, "role": "Data Analyst"}


# 2. DICT CONSTRUCTOR CREATION
dict_from_tuples = dict([("city", "Lahore"), ("country", "Pakistan")])


# 3. ACCESSING VALUES USING KEYS
name = my_dict["name"]


# 4. ACCESSING VALUES USING GET() (SAFE ACCESS WITH DEFAULT VALUE)
salary = my_dict.get("salary", 0)


# 5. ADDING OR UPDATING A SINGLE KEY-VALUE PAIR
my_dict["age"] = 26
my_dict["department"] = "AI"


# 6. UPDATE() METHOD (BULK UPDATE OR MERGE)
my_dict.update({"salary": 75000, "role": "AI Engineer"})


# 7. SETDEFAULT() (INSERTS KEY WITH DEFAULT IF NOT PRESENT, RETURNS VALUE)
status = my_dict.setdefault("status", "Active")


# 8. REMOVING A KEY USING DEL
del my_dict["department"]


# 9. REMOVING A KEY USING POP() (RETURNS THE REMOVED VALUE)
removed_salary = my_dict.pop("salary", None)


# 10. REMOVING AND RETURNING LAST INSERTED PAIR USING POPITEM()
last_pair = my_dict.popitem()


# 11. CHECKING KEY EXISTENCE (IN / NOT IN)
has_age = "age" in my_dict


# 12. GETTING ALL KEYS (.KEYS())
all_keys = list(my_dict.keys())


# 13. GETTING ALL VALUES (.VALUES())
all_values = list(my_dict.values())


# 14. GETTING ALL KEY-VALUE PAIRS (.ITEMS())
all_items = list(my_dict.items())


# 15. ITERATING THROUGH A DICTIONARY
for key, value in my_dict.items():
    pass


# 16. DICTIONARY COMPREHENSION
squared_evens = {x: x**2 for x in range(6) if x % 2 == 0}


# 17. MERGING DICTIONARIES USING '|' OPERATOR (PYTHON 3.9+)
dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}
merged_dict = dict_a | dict_b


# 18. COPYING A DICTIONARY (SHALLOW COPY)
dict_copy = my_dict.copy()


# 19. CLEARING ALL ITEMS FROM DICTIONARY
my_dict.clear()


# 20. DELETING THE DICTIONARY VARIABLE
del my_dict