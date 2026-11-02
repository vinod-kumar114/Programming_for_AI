# composition -> child ka object, parent ke init m banta hy

class Heart:
    def __init__(self):
        self.beat = True

class Human: # parent
    def __init__(self):
        self.heart = Heart() # building child object in parent init

# if no human, no heart will be there


# aggregation : Child ka object bahir banta hy, and phir parent ko pass kiiya jata hy

class Teacher:
    def __init__(self, name):
        self.name = name

class Dept:
    def __init__(self, teacher_obj):
        self.teacher = teacher_obj

t = Teacher("Shayan")

cs_dpt = Dept(t)

print(cs_dpt.teacher.name) # accessing the attributes of child class

del cs_dpt

print(t.name)
