# alien_color="red"
# if alien_color=="green":
#     print("The player just earned 5 points")
# elif alien_color=="yellow":
#     print("The player just earned 10 points")
# elif alien_color=="red":
#     print("The player just earned 15 points")



usernames=["admin", "student1", "student2", "teacher1", "teacher2"]

for name in usernames:
    if name=="admin":
        print("Hello admin, wouuld u like to see a status report.")
    else:
        print("Hello "+name+", thank you for logging in again.")