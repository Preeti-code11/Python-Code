
class Vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__vehicle_cost=None
        self.__premium_amount=None
        
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id=vehicle_id
        
    def set_vehicle_type(self, vehicle_type):
        if vehicle_type in ['Two Wheeler','Four Wheeler']:
            self.__vehicle_type=vehicle_type
        else:
            print("Invalid vehicle details")
        
    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost=vehicle_cost
        
    def set_premium_amount(self, premium_amount):
        self.__premium_amount=premium_amount
        
    def get_vehicle_id(self):
        return self.__vehicle_id
        
    def get_vehicle_type(self):
        return self.__vehicle_type
        
    def get_vehicle_cost(self):
        return self.__vehicle_cost
        
    def get_premium_amount(self):
        return self.__premium_amount
        
        
    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount=self.__vehicle_cost*2/100
        elif self.__vehicle_type=="Four Wheeler":
            self.__premium_amount=self.__vehicle_cost*6/100
        else:
            print("Invalid Vehicle Type")
        
    def display_vehicle_details(self):
            print("Vehicle id is", self.__vehicle_id)
            print("Vehicle type is", self.__vehicle_type)
            print("Vehicle cost is", self.__vehicle_cost)
            print("Vehicle premium is", self.__premium_amount)
        
v1=Vehicle()
v1.set_vehicle_id(100)
v1.set_vehicle_type("Two Wheeler")
v1.set_vehicle_cost(105000)
v1.calculate_premium()
v1.display_vehicle_details()
        