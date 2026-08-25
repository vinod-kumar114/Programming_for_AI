
#  to create a function in Python, we use "def" and a () paranthesis after the function name

# def greet():
#     print("Good Morning")
# for i in range(5):
#     greet() 

# def sum(a,b):
#     print(f"The sum of {a} and {b} is {a+b}")
# sum(13,12)



# ===== Types of arguments =====

# # Positional argument
# def subtract(w,e):
#     return w-e
# print(subtract(5,2))


# # keyword arguments
# def introduce(name, age):
#     print(f"My name is {name} and my age is {age} years")
# introduce("Vinod", 18) # regular kaam
# # if me chahta hu ke name baaad m add kru and age pehly, usky liye aisy krna prega
# introduce(age=18, name="Vinod")


# default argument
# kabhi agar hum khud se value na den to default values kaam kr sakti hen jaisy

# def intro(name="Unknown", age=18):
#     print(f"I am {name} and i am {age} years old")
# intro() # yaha agar me arguments na bhi du na to kaam chal jayega


# Check if the tring is a pellindrom or not

def pellindrome(str):
    rev=""
    for i in range(len(str)-1, -1, -1):
        rev+=str[i]
    if rev==str:
        print("Pellindrome")
    else:
        print("Not Pellindrome")

pellindrome("naman")