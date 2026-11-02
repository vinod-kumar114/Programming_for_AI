staff = [
    {"dept": "IT", "salary": 80000},
    {"dept": "HR", "salary": 60000},
    {"dept": "IT", "salary": 95000}
]

# Primary sort by dept (A-Z), secondary sort by salary (descending)
staff.sort(key=lambda x: (x["dept"], -x["salary"]))  
print(staff)