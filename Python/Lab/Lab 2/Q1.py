students = {
    "Ali" : {
        "Math":70, "Science":78, "English": 80, "Social Studies": 89
    },
    "Ahmed" : {
        "Math":80, "Science":88, "English": 85, "Social Studies": 84
    },
    "Dua" : {
        "Math":95, "Science":88, "English": 92, "Social Studies": 97
    }
}

threshold = 80
avgs = {}
highestAvg = 0
highestStd= " "
aboveAvg = []

for names , marks in students.items():

    totalMarks=sum(marks.values())

    totalSub=len(marks)

    avg=totalMarks/totalSub

    avgs[names]=round(avg, 2)

    if avg>highestAvg:
        highestAvg=avg
        highestStd = names

    if avg>=threshold:
        aboveAvg.append(names)

print("Student averages: ")
for std, avg in avgs.items():
    print(f"{std}: {avg}")

print("Highest performer: ")
print(f"{highestStd}")

print("Students above Threshold: ")
for std in aboveAvg:
    print(f"{std}")
