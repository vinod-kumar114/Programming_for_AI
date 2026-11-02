class Device:
    category = "Electronics"

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price


    def show_info(self):
        print("category: ", self.category)
        print("Brand: ", self.brand)
        print("Price: ", self.price)


d1 = Device("Oppo", 15000)

d1.show_info()