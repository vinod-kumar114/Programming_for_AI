import csv

headers = ["Name", "Age", "City"]
student = [
    ["Ali", 18, "Khi"],
    ["Fatima",19,"Hyd"],
    ["VK",18,"Hyd"]
]

with open("students.csv",mode="w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(student)

with open("students.csv", mode='r') as file:
    reader = csv.reader(file)
    for r in reader:
        print(r)

newstd = ["Dua",19,"Khi"]

# with open("students.csv", mode='a',newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(newstd)

with open("students.csv", mode='r') as file:
    reader = csv.reader(file)
    for r in reader:
        print(r)
