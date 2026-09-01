"""7.An online shopping application allows customers to add products to a shopping cart, remove products, modify
quantities, and calculate the total price.A product may appear only once in the cart, but its quantity can
change.Design a suitable data representation for the shopping cart and implement the required operations.
Requirement: Think carefully about whether a simple list is sufficient for this problem."""

cart = {
    "product1":{"quantity":2, "price": 100},
    "product2":{"quantity":4, "price": 200}
}

print("Add product: ")
cart["product3"] = {"quantity": 1, "price":50}
print(cart)

print("Delete product: ")
del cart["product1"]
print(cart)

print("Modify quantity: ")
cart["product2"]["quantity"]+=2
print(cart["product2"])

print("Total price: ")
cart_total=0
for i, j in cart.items():
    product_total=0
    product_total+=(j["quantity"]*j["price"])
    print(f"Total price for {i} is: ", product_total)
    cart_total+=product_total

print("Total price of cart is: ", cart_total)