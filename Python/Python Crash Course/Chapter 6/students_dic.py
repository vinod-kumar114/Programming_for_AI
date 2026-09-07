students = {
    "Muhammad": "25k-0001",
    "Fatima": "25k-0002",
    "Rahul": "25k-0003",  
    "Aisha": "25k-0004",
    "Ali": "25k-0005",
    "Anjali": "25k-0006",  
    "Hamza": "25k-0007",
    "Zainab": "25k-0008",
    "Amit": "25k-0009",  
    "Bilal": "25k-0010",
}


# ============= keys only =============
# for name in students:
#     print(name)
# # 2nd way
# for name in students.keys():
#     print(name)

# ========== values only =============
# for id in students.values():
#     print(id)


# ========== key-value pair ===========

# # ===== 1st way: =====
# for name, id in students.items():
#     print(f"{name} : {id}")

# # ====== 2nd way: =====
# for items in students:
#     print(f"{items} : {students[items]}")


# This is the list of students who got positions:
position_holders = {"Rahul":"1st", "Bilal":"2nd", "Zainab":"3rd"}

# Meessage to appreciate them 

for name in students:
    if name in position_holders:
        print(f"{name} with roll no. {students[name]} got the {position_holders[name]} position.")