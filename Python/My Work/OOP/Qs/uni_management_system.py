class Classroom:
    def __init__(self, roomCode, roomName):
        self.roomCode = roomCode
        self.roomName = roomName

class Faculty:
    def __init__(self, fullName, employeeID):
        self.fullName = fullName
        self.employeeID = employeeID


class Department:
    def __init__(self, name):
        self.name = name
        self.classrooms = []
        self.faculty = []

    def addClass(self, rcode, rname):
        new_class = Classroom(rcode,rname)
        self.classrooms.append(new_class)

    def assignFaculty(self, fac_obj):
        self.faculty.append(fac_obj)

    def displayDetails(self):
        print("Department name:",self.name)
        print("Faculty: ")
        for f in self.faculty:
            print(f.fullName, f.employeeID)

        print("Classrooms: ")
        for cls in self.classrooms:
            print(cls.roomCode, cls.roomName)


t1 = Faculty("Vinod", 250114)

cs = Department("CS")

cs.addClass("PY", "Lab 7")
cs.addClass("OOP", "Lab 7")

cs.assignFaculty(t1)

cs.displayDetails()