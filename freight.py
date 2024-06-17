class Freight:

    counter=198

    def __init__(self, recipient_customer, from_customer, weight, distance):
        self.__recipient_customer=recipient_customer
        self.__from_customer=from_customer
        self.__weight=weight
        self.__distance=distance

    def get_recipient_customer(self):
        return self.__recipient_customer

    def get_from_customer(self):
        return self.__from_customer

    def get_freight_id(self):
        return self.__freight_id

    def get_freight_charge(self):
        return self.__freight_charge
        

    def validate_weight(self):
        if (self.__weight)%5==0:
            return True
        else:
            return False

    def validate_distance(self):
        if (self.__distance>=500 and self.__distance<=5000):
            return True
        else:
            return False

    def forward_cargo(self):
        self.__freight_id=200
        if (self.__from_customer.validate_customer_id() and self.__recipient_customer.validate_customer_id() and self.validate_distance() and self.validate_weight()):
            self.__freight_id=self.__freight_id
            self.__freight_charge=(150*self.__weight+60*self.__distance)
            print("Freight id is ", self.__freight_id)
            print("Freight charge is ", self.__freight_charge)

        else:
            self.__freight_charge=0
            print("Invalid Entry")
        self.__freight_id=self.__freight_id+2


        


class Customer:

    def __init__(self, customer_id, customer_name, address):
        self.__customer_id=customer_id
        self.__customer_name=customer_name
        self.__address=address

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_nmae(self):
        return self.__customer_name

    def get_address(self):
        return self.__address

    def validate_customer_id(self):
        if ((int(self.__customer_id/100000))==1):
            return True
        else:
            return False

c1=Customer(123456, "Preeti", "b58,jhn1")
c2=Customer(123457, "Ankit", "pune")
f1=Freight(c1, c2, 5, 1000)
f1.forward_cargo()
    
