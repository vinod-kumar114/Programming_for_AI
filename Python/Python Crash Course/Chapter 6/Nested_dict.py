

# ============ A list of dictionaries ==================

# we use it to store many kinds of info about one object. 
# It is easy to access one complete object and its characteristics

# alien_0 = {'color':'green', 'points':5}
# alien_1 = {'color':'red', 'points':10}
# alien_2 = {'color':'yellow', 'points':15}


# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# we can access any key in the list of dict in this way:
# print(aliens[0]['color'])

# we can create a list of more aliens using loop and range func, but the issue would be that thay all will have same characteristics

# aliens=[]
# for alien in range(30):
#     new_alien = {'color':'red', 'points':15, 'speed':'fast'}
#     aliens.append(new_alien)

# for alien in aliens[:5]:
#     print(alien)

# print(len(aliens))

# If we want to have changes in the aliens then we can use if statements and their keys to change their characteristics
# Example: we want to change color, points, speed of 1st 7 aliens

# for alien in aliens[:7]:
#     if alien['color']=='red':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10

# for alien in aliens[:10]:
#     print(alien)




# ============= A list in a Dictionary ==============

# a list in a dictionary is useful when we want other things and same things as well. For example, I have to describe a student. I will store his name, roll no, and a list of courses he is studying.abs

# student = {
#     'name':'Vinod Kumar',
#     'Roll_No':'25k-0114',
#     'courses':['PAI', 'DSA', 'LA', 'COAL']
# }

# print(student['name']+' with roll no '+student['Roll_No']+' studies the following courses at FAST: ')
# for course in student['courses']:
#     print(course, end = ', ')

# If we ask studets about their fvt languages, they could be more than one

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']}
    
# # when we loop through the dictionary, the value associated with each person would be a list of languages, rather than a single language
# # in the dict's for loop, we use another for loop to run through the list of languages associated with each person.abs

# for name, languages in favorite_languages.items():
#     print(name.title(),"'s favourite languages are: ")
#     for language in languages:
#         print("\t\t\t\t",language.title())


#  in 1st for loop, varibale 'name' represents keys, and  variable 'languages' holds each value from dict: the value means the list.
# we use another for loop to run through the list of languages





# ============= A Dictionary in a Dictionary ==============

# if u have several users for a website, with a unique username, u can use the usernames as the keys in a dictionary. U can store info about each user by using a dictionary as a value associated with their usernme. 

# my_followers = {
#     "iam_sagar": {'f_name':'Daim', 'l_name':'Sagar', 'email':'daim@gmail.com'},
#     "iam_girdharilal": {'f_name':'Girdhari', 'l_name':'Lal', 'email':'girdhari@gmail.com'},
#     "iam_vinesh": {'f_name':'Vinesh', 'l_name':'Prikash', 'email':'vinesh@gmail.com'},
# }

# for u_name, info in my_followers.items():
#     print("Username: "+u_name)
#     print("Full name:", info['f_name']+" "+info['l_name'])
#     print("Email:", info['email'], "\n")

