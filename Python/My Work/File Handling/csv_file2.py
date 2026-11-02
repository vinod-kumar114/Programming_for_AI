import csv

p = [
    ["ID","Age","Glucose","Diabetes"],
    [1,45,148,1],
    [2,32,85,0],
    [3,50,180,1],
    [4,28,115,0],
]

with open("patients.csv", mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(p)
count = 0
with open("patients.csv", mode="r", newline="") as f:
    reader = csv.DictReader(f)
    count = 0
    for row in reader:
        if int(row["Diabetes"]) == 1:
            count+=1
        if int(row["Glucose"])>130:
            print(row)

print("Total patients having diabetes: ", count)
