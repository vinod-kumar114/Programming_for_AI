"""Create a Python program for an online shopping system. 

Create a class Product with attributes name and price. Create a class DiscountedProduct that extends Product. Add an additional attribute discount. Create a method final_price() that calculates and displays the price after discount. Create at least two objects and test the program."""

class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price


class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name,price)
        self.discount = discount

    def final_price(self):
        disc_price = self.price * ((100-self.discount)/100)
        print("Product:", self.name)
        print("Original Price:", self.price)
        print("Price after discount:", disc_price)

p1 = DiscountedProduct("Aloe vera", 150, 10)
p2 = DiscountedProduct("Face Wash", 750, 15)

p1.final_price()
p2.final_price()