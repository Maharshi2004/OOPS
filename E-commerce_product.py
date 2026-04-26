# Encapsulation Task 1: E-Commerce Product
# 📌 Instructions:
# Create a class Product
# Create private variable for price
# Add method set_price(price)
# Accept only values greater than 0
# Add method apply_discount(percent)
# Discount should not exceed 50%
# Update price after discount
# Add method get_price()
# Return current price

class Product:
    def __init__(self):
        self.__price = 0
    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            print("Price must be greater than 0")
    def apply_discount(self, percent):
        if 0 < percent <= 50:
            discount_amount = (self.__price * percent) / 100
            self.__price -= discount_amount
        else:
            print("Discount should be between 0 and 50%")
    def get_price(self):
        return self.__price
p1 = Product()
p1.set_price(int(input("enter amount: ")))
p1.apply_discount(int(input("Enter percent: ")))
print(p1.get_price())