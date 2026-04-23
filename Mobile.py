class Mobile:
    brand = "Apple"
    def set_details(self):
        self.model = "iPhone 14"
        self.price = 80000
    def discount(self):
        self.price = self.price - (self.price * 10) / 100
    def show_details(self):
        print(self.model)
        print(self.price)
b = Mobile()
b.set_details()
b.discount()
b.show_details()
print(Mobile.brand)