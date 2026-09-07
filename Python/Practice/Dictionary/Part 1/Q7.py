# Loop — Sorting Dictionary Data

# Given a dictionary of employees and their salaries, create a list of (employee, salary) tuples sorted in descending order of salary, and print only the top 3 highest-paid employees.

salaries = {'Ahmed': 95000, 'Farah': 120000, 'Saad': 78000, 'Mahnoor': 135000, 'Bilal': 60000}


sorted_salaries=sorted(salaries.items(), key=lambda x: x[1], reverse=True)

for key,value in sorted_salaries[:3]:
    print(f"{key}: {value}")