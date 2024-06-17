flowers=['ORCHID','ROSE','JASMINE']
levels=[15,25,40]
class Flower:
    def __init__(self, flower_name, price_per_kg, stock_available):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
    
    def set_flower_name(self, flower_name):
        self.__flower_name=flower_name

    def set_price_per_kg(self, price_per_kg):
        self.__price_per_kg=price_per_kg

    def set_stock_available(self, stock_available):
        self.__stock_available=stock_available

    def get_flower_name(self):
        return self.__flower_name
    
    def get_price_per_kg(self):
        return self.__price_per_kg

    def get_stock_available(self):
        return self.__stock_available

    def validate_flower(self):
        if self.__flower_name.upper() in Flower.flowers:
            return True
        else:
            return False

    def validate_stock(self, required_quantity):
        if self.__stock_available>=required_quantity:
            return True
        else:
            return False

    def sell_flower(self, required_quantity):
        if self.validate_flower and self.validate_stock:
            self.__stock_available=self.__stock_available-required_quantity

    def check_level(self):
        if self.validate_flower():
            flower_level=Flower.levels[Flower.flowers.index(self.__flower_name.upper())]
            if self.__stock_available<flower_level:
                return True
        else:
            return False
            print("Not available")
        

f1=Flower("Rose", 24, 20)
f1.set_flower_name("Rose")
f1.set_price_per_kg(24)
f1.set_stock_available(20)
f1.validate_flower()
f1.validate_stock(20)
f1.sell_flower(20)
f1.check_level()