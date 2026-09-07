"""
Types of function wrt ARGUMENTS
    1. Positional
    2. Keyword
    3. Default
"""


# ========== POSITIONAL ==============
# In positional, the order of arguments matter

# def info(name, age):
#     print("Name:", name)
#     print("Age:", age)

# # info("Vinod", 18) # this is the correct order

# # but what if we interchange the order, it will not the required output
# info(18,"Vinod") # not a suitable order



# ========== KEYWORD ==============
# a name-value pair that we passs to the func

# def info(name, age):
#     print("Name:", name)
#     print("Age:", age)

# info(name="Vinod", age=18)  # main game is here. 
# info(age=18, name="Vinod")  # it too will give anser in right order



# ========== DEFAULT ==============
# while writing a function, we can give default values in the parametrs as well

def info(name="unknown", age=18):
    print("Name:", name)
    print("Age:", age)

info()
info("Ali")

# now either we provide arguments or not, we will get the output

# if we are providing only a single default value, then it should be placed in the last of the parameter list

def info(name, age=18):  # here, we can't put default parameter first
    print("Name:", name)
    print("Age:", age)