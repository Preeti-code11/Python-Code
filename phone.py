class Phone:
    def __init__(self, price, brand, camera):
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone.")

    def return_phone(self):
        print("Returning a phone.")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

Phone(1000,"Apple",13).buy()
s=SmartPhone(20000,"Apple",13)