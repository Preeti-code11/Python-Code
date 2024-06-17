class Customer:
    def __init__(self, customer_name):
        self.__customer_name=customer_name

    def pays_bill(self, bill):
        self.__payment_status="Paid"
        print("Customer name is ", get_customer_name())
        print("Bill id is ", get_bill_id())
        print("Bill amount is ", get_bill_amount())
        
    
    def get_customer_name(self):
        return self.__customer_name

    def get_payment_status(self):
        return self.__payment_status


class Bill:
    counter=1000
    def __init__(self, item):
        self=None
        self.item=item
        
    def generate_bill_amount(self, item_quantity, item):
        self.item_quantity = item_quantity
        self.item = item
        
        for item in list_of_items:
            print (item.item_id,item.__price_per_quantity)

        
        
        

    def get_bill_id(self):
        self.__bill_id = "B"+str(counter+1)
        return self.__bill_id

    def get_bill_amount(self):
        self.__bill_amount=0
        for key,value in self.item_quantity.items():
            self.__bill_amount+=(self.item_quantity[key])*(self.items[Item.price_per_quantity])
        return self.__bill_amount
        

b1 = Bill()
b1.generate_bill_amount({'ir658':4, 'IR123':2, 'IR987':3, 'Ir346':2}, )


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

i1=Item(IR987, 'Sunfeast Marie', 100.0)
i2=Item(ir658, 'Kellogs Oats', 151.0)
i3=Item(Ir346, 'Maggie Noodles', 35.75)
i4=Item(iR234, 'Kissan Jam', 100.0)
i5=Item(IR123, 'Nescafe', 55.5)
i6=Item(IR111, 'Milk', 100.0)
list_of_items = [i1,i2,i3,i4,i5,i6]



