

# ================== Pattern 3: Nested Dictionary containing List of Dictionaries =====
# ================== (Complex Organizational / University Portal Data) ================


# 1. DATA STRUCTURE
university = {
    "CS_Dept": {
        "head": "Dr. Arshad",
        "faculty": [
            {"name": "Usman", "designation": "Lecturer", "salary": 120000},
            {"name": "Ayesha", "designation": "Assistant Prof", "salary": 200000}
        ]
    },
    "AI_Dept": {
        "head": "Dr. Zafar",
        "faculty": [
            {"name": "Bilal", "designation": "Lecturer", "salary": 130000},
            {"name": "Hamza", "designation": "Associate Prof", "salary": 250000}
        ]
    }
}

for v in university.values():
    for member in v["faculty"]:
        if member["designation"] == "Lecturer":
            member["salary"] *= 1.1

print(university)
 
# 2. ACTION: Specific designation walon ka salary increment karna (10%)
# for dept, dept_info in university.items():
#     print(f"\nDepartment: {dept} (Head: {dept_info['head']})")
    
#     for member in dept_info["faculty"]:
#         if member["designation"] == "Lecturer":
#             member["salary"] *= 1.10  # 10% increment
            
#         print(f" - {member['name']} ({member['designation']}): New Salary = {member['salary']:.0f}")