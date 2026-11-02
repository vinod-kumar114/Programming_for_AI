# alien = {'color': 'green', 'points':5}
# # print(alien['color'])   # values are accessed in this way

# alien ['x-coordinate']=0
# alien ['y-coordinate']=25

# print(alien)

# # changing position of alien:
# alien = {"x":0, 'y':25, 'speed':'medium'}
# if alien['speed']=='slow':
#     alien['x']+=1
# elif alien['speed']=='medium':
#     alien['x']+=2
# else:
#     alien['x']+=3

# print(f"({alien['x']}, {alien['y']})")


# friend = {"f_name":"Daim", "l_name":"Sagar", "age":18, "city":"Sukkar"}

# # print(list(friend.items())[0])
# for key, value in friend.items():
#     print("\nKey: "+key)
#     print("Value: "+str(value))



# Key-value pair

fvt_language={
    "Ali":"C++",
    "Dua":"Python",
    "Ahmed":"Java",
    "Muaaz":"Python"
}
# for name, language in fvt_language.items():
#     print(name.title(),":",language.title())


# Only keys:
# for name in fvt_language.keys():
#     print(name)


# Only values:
# for language in fvt_language.values():
#     print(language)

# if keys and values in diff lists:
# for items in fvt_language.keys(), fvt_language.values():
#     print(f"{items}")


# friends = ["Ahmed", "Muaaz"]

# for name in fvt_language.keys():
#     if name in friends:
#         print(f"Hi {name}, I see your favourite language is {fvt_language[name]}")



# to get rid of same values, we can use SET

for language in set(fvt_language.values()):
    print(language)
