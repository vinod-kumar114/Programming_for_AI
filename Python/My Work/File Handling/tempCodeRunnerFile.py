with open("students.csv", mode='a',newline="") as file:
    writer = csv.writer(file)
    writer.writerow(newstd)