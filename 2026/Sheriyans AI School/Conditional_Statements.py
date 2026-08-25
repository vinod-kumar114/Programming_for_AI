# In python the indentation matters for the flow. In C or C++ we use {}, but in python we rely on spaces 

# else if : elif

# # a = 10
# a = 1

# if a > 10:
#     print("I will do task A")

# else:
#     print("I will do task B")


# pocketMoney = int(input("Please give me some money: "))
# if pocketMoney >0 and pocketMoney <20:
#     print("NOt enough money to buy something")
# elif pocketMoney >= 10 and pocketMoney <20:
#     print("Buy Biscuit")
# elif pocketMoney >= 20 and pocketMoney <30:
#     print("Buy Icecream")
# else:
#     print("Buy Chocolate")


# # Q1:Accept two numbers and print the greatest between them.

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# if num1>num2:
#     print(f"{num1} is greater than {num2}")
# elif num2>num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both numbers are equal")


# Q2: Accept the gender from the user as char and print the respective greeting message 

# gender = input("Enter your gender (m/f):")
# if gender == 'm':
#     print("Good Morning Sir")
# elif gender== 'f':
#     print("Good Morning Mam")
# else:
#     print("Incorrect input")


# Q3. Accept an integer and check whether it is an even number or odd.

# num = int(input("Enter a number: "))
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")


# Q4. Accept name and age from the user. Check if the user is a valid voter or not.

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age >= 18:
#     print(f"Hello {name}, you are a valid voter")
# else:
#     print(f"Hello {name}, you are not a valid voter")


# # Q5. Accept a year and check if it a leap year or not

# year = int(input("Enter a year: "))
# if year%4==0 :
#     if year%100==0 and year%400!=0:
#         print(year, "is not a leap year")
#     else:
#         print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")


# Q6. take the input of temperature in celsius
#     Below 0°C → "Freezing Cold 
#     0°C to 10°C → "Very Cold 
#     10°C to 20°C → "Cold 
#     20°C to 30°C → "Pleasant 
#     30°C to 40°C → "Hot 
#     Above 40°C → "Very Hot "

# temp = int(input("Enter temperature in Celsius: "))
# if temp<0:
#     print("Freezing Cold")
# elif temp >=0 and temp<10:
#     print("Very Cold")
# elif temp>=10 and temp<20:
#     print("Cold")
# elif temp >=20 and temp<30:
#     print("pleasant")
# elif temp>=30 and temp <40:
#     print("Hot")
# else:
#     print("Very Hot")