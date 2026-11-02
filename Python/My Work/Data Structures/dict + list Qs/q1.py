

# ========= Pattern 1: Nested Dictionary with Inner List ==========
# ========== (Standard Student Record & Grade Processor) ==========


# 1. DATA STRUCTURE
students_data = {
    "FAST-001": {
        "name": "Ali",
        "courses": ["AI", "PF", "OOP"],
        "marks": [85, 90, 78]
    },
    "FAST-002": {
        "name": "Sara",
        "courses": ["AI", "Calculus"], 
        "marks": [92, 88]
    }
}

for val in students_data.values():
    for i in zip(val["courses"],val["marks"]):
        print(i)

# # 2. ACTION: Average marks calculate kar ke student record me naya key add karna
# for roll_no, info in students_data.items():
#     total_marks = sum(info["marks"])
#     avg_marks = total_marks / len(info["marks"])
#     # Dynamic action: Naya field update karna
#     info["average"] = round(avg_marks, 2)


# # 3. ACCESS & DISPLAY
# print("--- STUDENT MARKS REPORT ---")
# for roll_no, info in students_data.items():
#     print(f"Roll No: {roll_no} | Name: {info['name']}")
#     for course, mark in zip(info["courses"], info["marks"]):
#         print(f"   -> Course: {course} | Mark: {mark}")
#     print(f"   --> Average: {info['average']}\n")