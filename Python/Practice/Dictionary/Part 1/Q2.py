""" Q2. Basic — Accessing Values Safely

You are given a dictionary of country–capital pairs. Ask the user to enter a country name and print its capital. If
the country is not in the dictionary, print "Capital not found" instead of causing an error (use an appropriate
dictionary method rather than square-bracket indexing).

capitals = {'Pakistan': 'Islamabad', 'Japan': 'Tokyo', 'France': 'Paris'}"""

capitals = {'Pakistan': 'Islamabad', 'Japan': 'Tokyo', 'France': 'Paris'}
search = input("Enter a country: ")
found = False
for key, value in capitals.items():
    if key.lower() == search.lower():
        print(value)
        found = True
if not found:
    print("Capital not found")