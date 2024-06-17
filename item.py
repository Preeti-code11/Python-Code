
class Item:
    def __init__(self, item_id, description, price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity

    def get_item_id(self):
        return self.__item_id

    def get_description(self):
        return self.__description

    def get_price_per_quantity(self):
        return self.__price_per_quantity

item1 = Item(101, "Sugar", 50)
item2 = Item(102, "Salt", 20)
item3 = Item(103, "Tea", 240)
        
dict_of_items = { "i1":item1,
                  "i2":item2,
                  "i3":item3
                 }

for key,value in dict_of_items.items():
    if value.get_price_per_quantity() > 20:
        print (value.get_item_id(), value.get_description())