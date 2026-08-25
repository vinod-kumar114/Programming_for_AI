# Python Strings: 
# Strings in Python are identified as a contiguous set of characters represented in the quotation marks. Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the slice operator ([ ] and [:] ) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end.

str = 'Hello World'
print(str) # prints whole string
print(str[0]) # prints the first character of the string
print(str[2:5]) # starting from 3rd to 5th character: isme aisa ni hoga ke 5th index ko bhi print krega, balky isme bs index 2, 3, and 4 ko print krega. 5 is the end point. So agar kabhi bhi aisa aye to hum kia assume krengy ke ye n-1 index tak print krega. 

print(str[0:])
print(str*2) # prints the string 2 times without any space bw
print(str+" Python") # prints 'Python' after printing the string