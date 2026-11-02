

class Doctor():
    def __init__(self, doct_name, doct_id):
        self.doct_name=doct_name
        self.doct_id=doct_id


class Ward():
    def __init__(self, w_name, w_code):
            self.w_name=w_name
            self.w_code=w_code


class Department():
    def __init__ (self, d_name):
        self.d_name=d_name
        self.doctList = []
        self.wardList = []

    def addWard(self,name,code):
        self.w = Ward(name,code)
        self.wardList.append(self.w)

    def assignDoct(self,d :Doctor):
            self.doctList.append(d)

    def display(self):
        print("Department: ",self.d_name)
        print("Doctors: ")
        for i in self.doctList:
            print(i.doct_name,i.doct_id)
        print("Wards: ")
        for j in self.wardList:
            print(j.w_name,j.w_code)

d1 = Doctor("Ali", "123")
# w1 = Ward("Sugar","ICU-01")
dept = Department("Health")
dept.addWard("Sugar","ICU-01")
dept.assignDoct(d1)
dept.display()


    