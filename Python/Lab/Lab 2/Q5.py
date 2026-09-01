"""5.An organization stores employee information such as employee ID, name, department, salary, and job title.Create
a system capable of handling operations such as searching for an employee, updating salary information, adding new
employees, and removing employees who leave the organization.
Requirement: The system should prioritize efficient employee lookup rather than sequential searching."""

employees = {
    "101":{"name":"Ali", "dept":"Ai", "salary": 1000, "title":"head"},
    "102":{"name":"Aliyan", "dept":"Ai", "salary": 1000, "title":"worker"}
}

searchId = "101"
print("Search Result:")
if searchId in employees:
    print(employees[searchId])
else:
    print("employee not found")

print("Update salary: ")
Id="102"
if Id in employees:
    employees[Id]["salary"]=1200
    print(employees[Id])

print("Adding new employee: ")
newId = "103"
employees[newId]={"name": "Usman", "dept": "CS", "salary": 1500, "title": "developer"}
print(employees[newId])


print("Removal: ")
Id="101"
if Id in employees:
    del employees[Id]
    print(f"emploee with id {Id} removed")
else:
    print("No any employee exists")
     
print(employees)