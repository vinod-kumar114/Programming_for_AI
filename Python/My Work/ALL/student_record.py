class Student:
    def __init__(self, name, roll):
        self.name=name
        self.roll=roll
        self.marks={}
        self.courses=[]

    def enroll_course(self, c):
        if c not in self.courses:
            self.courses.append(c)
            self.marks[c]=0
            print("course added")
        else:
            print("course already exists")

    def add_marks(self,marks, c):
        if c in self.courses:
            self.marks[c] = marks
            print("marks added")
        else:
            print("student not enrolled in courses")

    def generate_report(self):
        print(f"\--- Transcript for {self.name} ({self.roll}) ---")
        print(f"Total Courses: {len(self.courses)}")
        
        # Dictionary par loop lagana
        for course, score in self.marks.items():
            print(f"Subject: {course} | Marks: {score}")
        print("-" * 30)

# --- Object Creation & Usage ---
s1 = Student("Ali", "F22-101")

s1.enroll_course("Python")
s1.enroll_course("Calculus")

s1.add_marks("Python", 85)
s1.add_marks("Calculus", 78)
s1.add_marks("Physics", 90) # Ye error dega kyunke Physics me enroll nahi hai

s1.generate_report()