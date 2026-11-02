student = {'name':'shiva','age':32,'city':'hyderabad'}

student['Grade'] = 'A'
student['city'] = 'Delhi'
student.pop('age')

print(student)

if 'Grade' in student:
    print("Grade exists")
else:
    print("Not found")

for key in student.keys():
    print(key)

for value in student.values():
    print(value)

copy = student.copy()
student['grade'] = 'A'
print("original:",student)
print("copy:",copy)

# Get the value of a key safely using get() method (even if key not present).
student = {'name':'shiva','age':32,'city':'hyderabad'}
print(student.get('city','key not found'))

# count the total number of keys in the dictionary
print("Total keys:",len(student))

# Print the name of the student whose roll number is "102".
students = {
    "101":{"name":"amit","age":20},
    "102":{"name":"anuj","age":30},
    "103":{"name":"sai","age":32}
}
print(students["102"]["name"])

# Merge two dictionaries
a = {"x":10,"y":20}
b = {"y":30,"z":40}

a.update(b)
print(a)

# a program to find the key with the maximum value in a dictionary
dic = {"a":10,"b":90,"c":30,"d":70,"e":50}
max_key = max(dic,key = dic.get)
print(max_key)

max_value = max(dic.values())
print(max_value)

# a program to find the sum of all values in a dictionary
data = {'a':10,'b':20,'c':30}
total = sum(data.values())
print(total)

# Count how many times each word appears in a given list and store result in a dictionary
l = ["apple","banana","apple","mango","banana","apple"]
cont = {}
for w in l:
    if w in cont:
        cont[w] += 1
    else:
        cont[w] = 1
print(cont)

# Create a dictionary of marks and print only students who scored more than 75.
marks = {'sai':71,'raj':75,'anuj':78,'aman':80,'tarun':68}
for name,number in marks.items():
    if number > 75:
        print(name,":",number)

dic = {"a":10,"d":90,"c":30,"e":70,"b":50}
print(dict(sorted(dic.items())))

sort_lst = dict(sorted(dic.items(),key = lambda x: x[1]))
print(sort_lst)

# From a dictionary of items and prices, print the item with the lowest price.
pro = {'soap':50,'sugar':100,'oil':200,'ghee':800}
min_item = min(pro, key = pro.get)
print(min_item)

min_key = None
min_value = None
for key in pro:
    if min_value is None or min_value > pro[key]:
        min_value = pro[key]
        min_key = key
print(min_key)
print(min_value)

max_key = None
max_value = None
for key in pro:
    if max_value is None or max_value < pro[key]:
        max_value = pro[key]
        max_key = key
print(max_key)
print(max_value)

# Convert two lists into a dictionary
key = ['A','B','C','D','E','F','G','H','I','J','K','L']
value = [1,2,3,4,5,6,7,8,9,10,11,12]
result = {}
for i in range(len(key)):
    result[key[i]] = value[i]
print(result)

print(dict(zip(key,value)))

s = "aaabbcca"
result = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        result += s[i] + str(count)
        count = 1

result += s[-1] + str(count)
print(result)

s = "a3b2c2a1"
result = ""
for i in range(0,len(s),2):
    char = s[i]
    count = int(s[i+1])
    result += char * count
print(result)

# Create a dictionary of 5 products and their prices.
# Print all products whose price is between 100 and 200.
item = {'soap':50,'oil':200,'maggie':110,'sugar':90,'rice':300}
for item, prize in item.items():
    if 100 <= prize <= 200:
        print(item,"-",prize,"₹")

# Write a program to swap keys and values in a dictionary.
d = {'a':1,'b':2,'c':3}
swapped = {v: k for k,v in d.items()}
print(swapped)

# a program to count the frequency of characters in a given string using a dictionary.
s = "hello"
d = {}
for ch in s:
    if ch in d:
        d[ch] += 1
    else:
        d[ch] = 1
for k,v in d.items():
    print(k,"-",v,"times")

# a program to remove all duplicate values from a dictionary.
data = {'a':10,'b':20,'c':10,'d':30}
unique = {}
for k,v in data.items():
    if v not in unique.values():
        unique[k] = v
print(unique)

# Create a dictionary of students and their marks.
# Find the average marks of all students.
students = {'raj':75,'anuj':85,'sai':80,'tarun':60}
value = []
for k,v in students.items():
    value.append(v)
avg = sum(value)/len(value)
print("Total average marks:",avg)

avg = sum(students.values())/len(students)
print("Average marks:",avg)

# Create a dictionary and print the highest scorer.
names = ["Amit", "Raj", "Vikram"]
scores = [85, 90, 75]
data = {}
for i in range(len(names)):
    data[names[i]] = scores[i]
print(data)

highest_name = None
highest_score = 0
for name,score in data.items():
    if score > highest_score:
        highest_score = score
        highest_name = name
print("Highest scorer:",highest_name,"-",highest_score)

# Given a dictionary of employees and their salaries,
# increase every salary by 10% and print the updated dictionary.
employees = {'raj':30000,'sai':20000,'tarun':40000}
l = []
b = []
for k,v in employees.items():
    l.append(v)
    b.append(k)
print(l)
a = []
for i in l:
    data = i+(i*0.10)
    a.append(data)
print(a)

new_dic = {}
for i in range(len(b)):
    new_dic[b[i]] = a[i]
print(new_dic)

salary = {k:v + v*0.10 for k,v in employees.items()}
print(salary)

a = {'x': 10, 'y': 20}
b = {'y': 30, 'z': 40}
result = a.copy()
for k,v in b.items():
    result[k] = result.get(k,0)+v
print(result)

# a program to sort a dictionary by value in descending order.
data = {'a':1,'b':3,'c':4,'d':5,'e':2}
num = list(data.items())

for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i][1] < num[j][1]:
            num[i], num[j] = num[j], num[i]

sorted_desc = dict(num)
print(sorted_desc)

data = {"a": 5, "b": 20, "c": 10}
sorted_desc = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
print(sorted_desc)

# country with the maximum population.
country = {'India':140,'USA':25,'China':150,'America':40}
max_country = None
max_population = None
for n in country:
    if max_population is None or max_population < country[n]:
        max_population = country[n]
        max_country = n
print(max_country,"-",max_population)

max_country = max(country, key = country.get)
print(max_country)

# Write a program to create a dictionary from a string such that each unique word becomes a key
# and its count becomes value.
s = 'apple mango apple banana'
words = s.split()
result = {}
for n in words:
    if n in result:
        result[n] += 1
    else:
        result[n] = 1
print(result)

# Write a program that creates a dictionary using dictionary comprehension for numbers 1 to 5
square = {x: x**2 for x in range(1,6)}
print(square)

# using for loop
l = [1,2,3,4,5]
result = {}
for i in l:
    result[i] = i**2
print(result)

# You have a list of tuples, Convert it into a dictionary.
data = [('a',1),('b',2),('c',3)]
result = {}
for k,v in data:
    result[k] = v
print(result)

# Create a nested dictionary for employees,Print the salary of emp2
employee = {
  "emp1": {"name": "Amit", "salary": 30000},
  "emp2": {"name": "Sai", "salary": 35000}
}
name = employee['emp2']['name']
salary = employee['emp2']['salary']

print(name,"-",salary)

# Write a program to check if a dictionary is empty or not
data = {}
if not data:
  print("Empty")
else:
  print(data)

data = {'a':1,'b':2,'c':3,'d':4,'e':5}
pairs = []
for k,v in data.items():
  if k != 'a':
    pairs += [f"{k}:{v}"]
print(*pairs,sep=', ')

del data["b"]
print(data)