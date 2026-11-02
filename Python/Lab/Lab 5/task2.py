import csv
import os

file = "patients.csv"

def add(id, age, bmi, bp, glucose, diabetes):
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([id, age, bmi, bp, glucose, diabetes])

def display():
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def count_cases():
    if not os.path.exists(file):
        print("File does not exist.")
        return

    positive = 0
    negative = 0

    with open(file,"r",newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row["Diabetes"] =="1":
                positive+=1
            else:
                negative+=1

    print("Positive cases:", positive)
    print("Negative cases:", negative)

def glucose_check(threshold):
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if float(row["Glucose"])>threshold:
                print(row)

def average():
    if not os.path.exists(file):
        print("File does not exist.")
        return

    bmi_total = 0
    glucose_total = 0
    count = 0

    with open(file, "r", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            bmi_total += float(row["BMI"])
            glucose_total += float(row["Glucose"])
            count += 1

    print("Average BMI:", bmi_total / count)
    print("Average Glucose:", glucose_total / count)

def update(id, age, bmi, bp, glucose, diabetes):
    if not os.path.exists(file):
        print("File does not exist.")
        return

    with open(file, "r", newline="") as f:
        rows = list(csv.reader(f))

    found= False

    with open(file, "w", newline="") as f:
        writer = csv.writer(f)

        for row in rows:
            if row[0] == "ID":
                writer.writerow(row)
            elif row[0] == str(id):
                writer.writerow([id, age, bmi, bp, glucose, diabetes])
                found = True
            else:
                writer.writerow(row)

    if found:
        print("Patient updated successfully.")
    else:
        print("Patient does not exist.")


if not os.path.exists(file):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Age", "BMI", "Blood Pressure", "Glucose", "Diabetes"])

add(1, 45, 28.5, 130, 150, 1)
add(2, 32, 24.2, 120, 95, 0)
add(3, 50, 31.4, 140, 180, 1)

print("Patient records:")
display()

print("Diabetes cases:")
count_cases()

print("Patients with high glucose:")
glucose_check(120)

print("Average values:")
average()

add(4, 40, 27.8, 125, 110, 0)

print("After adding new patient:")
display()

update(2, 32, 25.1, 122, 130, 1)

print("after updating:")
display()

update(10, 30, 23.5, 118, 100, 0)