class Faculty:

    def __init__(self, name, employeeID):
        self.name = name
        self.employeeID = employeeID


class Course:

    def __init__(self, courseCode, courseTitle):
        self.courseCode = courseCode
        self.courseTitle = courseTitle


class Department:

    def __init__(self, name):
        self.name = name
        self.courses = []
        self.faculty = []

    def addCourse(self, code, title):
        course = Course(code, title)
        self.courses.append(course)

    def assignProfessor(self, professor):
        self.faculty.append(professor)

    def displayDetails(self):

        print("Department:", self.name)

        print("--- Courses Offered ---")

        for course in self.courses:
            print("-", course.courseCode, ":", course.courseTitle)

        print("--- Assigned Faculty ---")

        for professor in self.faculty:
            print("-", professor.name,
                  "(ID:", professor.employeeID + ")")


# Create department

department = Department("Computer Science")

# Add courses

department.addCourse("DS-5007", "Natural Language Processing")
department.addCourse("AI-2001", "Programming for AI")

# Create professors

p1 = Faculty("Dr. Muhammad Rafi", "EMP000")
p2 = Faculty("Mr. Talha Shahid", "EMP001")

# Assign professors

department.assignProfessor(p1)
department.assignProfessor(p2)

# Display

department.displayDetails()