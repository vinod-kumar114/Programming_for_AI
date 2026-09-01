"""A small e-commerce system maintains information about its products, including product ID, name, category, price,
and available quantity. The system should support product lookup, price updates, stock updates, and identification
of products that are out of stock. Requirement: Design the data representation so that product information can be
accessed efficiently using a unique identifier."""

product = {
    1 : {"name": "laptop", "category":"electronics", "price":10000, "quantity": 10},
    2 : {"name": "mobile", "category":"electronics", "price":5000, "quantity": 5},
    3 : {"name": "shirt", "category":"clothing", "price":1000, "quantity": 15},
}

# Product Look-up
searchId=2
print("Product Look-up: ")
print(product[searchId])

# price update
print("Price Update: ")
newPrice=12000
product[1]["price"]=newPrice
print(product[1])

# stock update
print("Stock Update: ")
newStock=  12
product[3]["quantity"]+=newStock
print(product[3])


for id, info in product.items():
    if info["quantity"]==0:
        print(f"ID {id} is out of stock")
