# Modes: 
# r -> reads file, only if file exists
# w -> removes previous data, and adds new
# a -> appends new data at the end of previous data
# r+ -> read and write both


file = open("data.txt","w")
file.write("Python course\n")
file.write("File handling\n")
file.close()

file = open("data.txt","r")
print(file.read())
file.close()

file = open("data.txt","a")
file.write("New data added\n")
file.close()


# Best and modren way:
with open("data.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)



# File ko delete krna:

# import os

# if os.path.exists("data.txt"):
#     os.remove("data.txt")
#     print("File removed")
# else:
#     print("FIle not found")