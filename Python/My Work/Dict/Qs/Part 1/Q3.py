"""Given an inventory dictionary mapping item names to quantities, print (a) all the keys, (b) all the values, (c) all
key-value pairs as tuples, and (d) the total number of items stored in the dictionary."""

inventory = {'Pen': 120, 'Notebook': 45, 'Eraser': 200, 'Ruler': 60}

# a. all keys
for key in inventory.keys():
    print(key)

# b. all values
for values in inventory.values():
    print(values)

# c. all kesy-value pairs as tuple
for key_value in inventory.items():
    print(key_value)

print(inventory)