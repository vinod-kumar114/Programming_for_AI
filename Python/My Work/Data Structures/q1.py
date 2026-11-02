db = [
    {"dept": "CS", "sections": {"A": [("Ali", 85), ("Sara", 45)], "B": [("Zain", 92), ("Omer", 30)]}},
    {"dept": "SE", "sections": {"A": [("Hira", 78), ("Raza", 39)]}}
]

# Task: Ek nested loop likho jo sirf un students ke naam print kare jinke marks 50 se kam hain, aur output format ye ho: "Omer from CS (Section B) failed with 30 marks."

for d in db:
    for key, val in d["sections"].items():
        for tup in val:
            if tup[1]<50:
                print(f"{tup[0]} from {d['dept']} section {key} failed with {tup[1]}")
