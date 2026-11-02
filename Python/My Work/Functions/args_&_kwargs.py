
#  *args
# arbitrary positional arguments

# 1. *args (Non-Keyword Arguments)
# When you don't know in advance how many positional arguments will be passed into your function, use *args. Inside the function, args becomes a tuple.

# def sum_all(*nums): # converts these in a tuple
#     s = 0
#     for n in nums:
#         s += n

#     print(f"Sum is {s}")

# sum_all(1,2,3,4,5,6,6)
# sum_all(14,56,69)


# def data(course,*marks, student): # correct format
#     print(student)
#     print(course)
#     print(marks)

# data("AI",23,24,24,student="Ali")




#  *kwargs
# arbitrary keyword arguments
# 2. **kwargs (Keyword Arguments)
# **kwargs allows you to pass any number of named/keyword arguments. Inside the function, kwargs becomes a dictionary.

def info(**person):
    for key, val in person.items():
        print(key,val)

info(name="ALi", age=18, dept = "AI", uni = "FAST")
info(name="Dua", age=18, dept = "AI")



# in functions 1st pass simple parameter, then args, then keyword, then kwargs
def display_info(required_arg, *args, status="Active", **kwargs):
    print(f"Required Argument: {required_arg}")
    print(f"Extra Positional (args): {args}")
    print(f"Default Argument (status): {status}")
    print(f"Extra Keyword (kwargs): {kwargs}")


display_info("FAST University", 10, 20, status="Pending", city="Lahore", gpa=3.8)