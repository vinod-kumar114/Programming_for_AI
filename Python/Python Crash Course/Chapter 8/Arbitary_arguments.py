# Sometimes you won’t know ahead of time how many arguments a function needs to accept. Fortunately, Python allows a function to collect an arbitrary number of arguments from the calling statement.

# pass single parameter with an asterick ( * )
# ( * ) tells python to create an empty tuple of parameter name and pack whatever values it recieves -> packs arguments in tuple


# def pizza(*toppings):
#     print("Apply these toppings on the pizza: ")
#     for topping in toppings:
#         print(" - "+topping)

# pizza("mushrooms","green peppers","extra cheese")




# NOTE: if u want to use several different kinds of arguments, the arbitary paramter must be placed last in the list

# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter.

# def make_pizza(size, *toppings): 
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a " + str(size) + 
#           "-inch pizza with the following toppings:") 
#     for topping in toppings: 
#         print("- " + topping) 
        
# make_pizza(16, 'pepperoni') 
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')






# ============ Arbitary Keyword Arguments ================

# Sometimes we want to pass many arguments and keep track of what kind of info we are passing

# we can define a func that accepts as many key-value pairs as much u want

# EXAMPLE: user profile: we know that we need info about user, but we are not sure what kind of info. 

# def build_profile(first,last, **user_info):
#     dic = {}
#     dic["first"] = first
#     dic["last"] = last
#     for key, value in user_info.items():
#         dic[key] = value

#     return dic

# profile = build_profile("Vinod","Kumar", age=18,department="AI", university="FAST")
# print(profile)



# def student(**info):
#     print(info)

# student(name="Ali", age=20, city="Karachi")