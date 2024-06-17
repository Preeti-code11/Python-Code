class Purchase:
    list_of_items=['Cake', 'Soap', 'Jam', 'Cereal', 'Hand Sanitizer', 'Biscuits', 'Bread']
    list_of_count_of_each_item_sold = 0

    def __init__(self):
        self=self
        self.__items_purchased = []
        self.__item_on_offer = None
    #def get_item_purchased():
    #def get_item_on_offer():
    
    def provide_offer():
        if soap in self.__items_purchased:
            self.__item_on_offer = "HAND SANITIZER"
            Purchase.list_of_count_of_each_item_sold += 1

    def sell_items(self, list_of_items_to_be_purchased):
        self.list_of_items_to_be_purchased=list_of_items_to_be_purchased
        Purchase.list_of_count_of_each_item_sold += len(self.list_of_items_to_be_purchased)
        for item in self.list_of_items_to_be_purchased:
            self.__items_purchased.append(item)

    def find_total_items_sold(self):
        return Purchase.list_of_count_of_each_item_sold

p1=Purchase()
list_of_items_to_be_purchased=['Jam', 'Cereal', 'Bread']
p1.sell_items(list_of_items_to_be_purchased)
p1.find_total_items_sold()


    