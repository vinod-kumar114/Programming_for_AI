
# value error: different data type ka input daa do, like required data int m hy, and hum string input de rhy hen
# try: 
#     age = int(input("Enter your age: "))
# except ValueError:
#     print("please enter integer data")


# Type error: different data types ki addition, concatenation, comparison. Same type ni hoty to ye error aata hy
# try:    
#     print("Age"+18)
# except TypeError:
#     print("Perform opeartion on same data type")


# Index Error: aisi index access krna jo available hi ni hy

# Key error: dict ki aisi key ko asccess krna jo dict m hy hi ni

# Name error: aisa variable access krna jo ke program m hy hi ni
# try:
#     print(a)
# except NameError:
#     print("Declare the variable")


# FileNotFound error: hum file ko access kr rhy hen, but wo exist hi ni krti



#  try m hum regular task krengy, and except m exception daal dengy, ke agar aisa aye to aisa kro. right. try m hamen kuchh extra condition ya if else ni lagana jis se exeption kaam kry

# try:
#     num1 = int(input("Enter numerator: "))
#     num2 = int(input("Enter denominator: "))
#     result = num1 / num2

# except ZeroDivisionError:
#     print("Error: Zero se divide nahi kar sakte!")

# except ValueError:
#     print("Error: Sirf integer numbers enter karein!")

# else:
#     print("Division Successful! Result:", result)

# finally:
#     print("Execution complete (Cleanup done).")


a = 18
b = int(input("Enter b: "))
try:
    if b == 0:
        raise ValueError("B can't be 0")

    print(a/b)

except ValueError as e:
    print('Error: ', e)
