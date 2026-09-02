"""10.A company provides the following information:
employees = [
    ("E101", "Ali", "IT", 85000),
    ("E102", "Sara", "HR", 75000),
    ("E103", "Ahmed", "IT", 95000),
    ("E104", "Zain", "Finance", 90000)
]
Develop a data-processing solution that can answer questions such as:
 Which employees belong to the IT department?
 What is the average salary?
 Who has the highest salary?
 Which departments exist?
 How many employees are in each department?
 Can an employee be efficiently retrieved using their employee ID? Requirement: You are expected to use
more than one Python data structure and justify why each structure was selected."""

employees = [
    ("E101", "Ali", "IT", 85000),
    ("E102", "Sara", "HR", 75000),
    ("E103", "Ahmed", "IT", 95000),
    ("E104", "Zain", "Finance", 90000)
]


# print("These employees belong to IT department: ")
# for i in employees:
#     if i[2]=='IT':
#         print(i[1])

# sum = 0
# for i in employees:
#     sum+=i[3]
# print("Average Salary: ",sum/len(employees))


# print("Frequency of employees in each department: ")
# dic = {}
# for i in employees:
#     dic[i[2]] = dic.get(i[2], 0)+1
# print(dic)


# An employee cannot be retrieved using their employee id in "List of tuples"