"""Given a dictionary of student names mapped to their marks (out of 100), loop through it and print the names of only those students who scored 80 or above."""

marks = {'Ayesha': 92, 'Bilal': 76, 'Zara': 85, 'Hamza': 58, 'Noor': 81}

for name, score in marks.items():
    if score>=80:
        print(name)