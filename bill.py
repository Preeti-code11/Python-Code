class Bill:
    def __init__(self, bill_id, patient_name):
        self.__bill_id=bill_id
        self.__patient_name=patient_name

    def calculate_bill_amount(self, consultation_fees, quantity_list, price_list):
        self.consultation_fees=consultation_fees
        total_price=0
        for i in range(0,len(quantity_list)):
            
            total_price=total_price+(quantity_list[i]*price_list[i])
        total_bill_amount=self.consultation_fees+total_price

        self.__bill_amount=total_bill_amount



    def get_bill_id(self):
        return self.__bill_id

    def get_patient_name(self):
        return self.__patient_name

    def get_bill_amount(self):
        return self.__bill_amount

b1=Bill(1001, "Preeti")
b1.calculate_bill_amount(500, [3,2,6], [200, 50, 100])
print(b1.get_bill_id())
print(b1.get_patient_name())
print(b1.get_bill_amount())