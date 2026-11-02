"""
Q2 You've been hired as a junior developer for "Karachi Readers," a small bookstore. The
manager wants a tool to check book stock and inventory value.
The current inventory is as follows:
 The Alchemist by Paulo Coelho — priced at PKR 1200, with 15 copies in stock.
 Forty Rules of Love by Elif Shafak — priced at PKR 1500, with 25 copies in stock.
 Sapiens by Yuval Noah Harari — priced at PKR 2200, with 10 copies in stock.
 Atomic Habits by James Clear — priced at PKR 1800, with 30 copies in stock.
Write a Python script to help the manager with the following tasks:
1. Represent the Inventory: Store the bookstore's inventory data within your program.
2. Check Stock: Allow the manager to input a Book Title and see the current stock count. If
the book is not in the inventory, display "Book not found."
3. Calculate Total Value: Calculate the total monetary value of the entire inventory.
4. Generate a Reorder List: Display the titles of all books with a stock count of 15 or less.
"""

inventory = {
    "The Alchemist":{"author":"Paulo Cohelo","price":1200,"stock":15},
    "Forty rules of love":{"author":"Elif Shafak","price":1500,"stock":25},
    "Sapiens":{"author":"Yoval Noh Harari","price":2200,"stock":10},
    "Atomic Habits":{"author":"James clear","price":1800,"stock":30}
}

# for key, value in inventory.items():
#     print(key,": ")
#     for k, v in value.items():
#         print(k,":",v)


# print(inventory)
def checkStock(b):
    found = False
    for tilte, values in inventory.items():
        if b==tilte.lower():
            print(values["stock"])
            found = True

    if found==False:
        print("Book not found")    

def total_value():
    total = 0
    for book in inventory.values():
        total+=(book["price"]*book["stock"])

    return total

def display_less_than_15():
    for book, values in inventory.items():
        if values["stock"]<=15:
            print(book)

print("Inventory: ")
print(inventory)
print()

b_name = input("Enter book title to check stock: ").lower()
checkStock(b_name)

print("\nTotal value of inventory: ")
print(total_value())

print("\nBooks with stock less than 15: ")
display_less_than_15()