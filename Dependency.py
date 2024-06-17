class Customer:
    def __init__(self,phone_no,name,age):
        self.phone_no=phone_no
        self.name=name
        self.age=age
        self.list_of_calls=None

class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.phoneno=phoneno
        self.called_no=called_no
        self.duration=duration
        self.call_type=call_type

class Util:
    def parse_customer(self,list_of_customers,list_of_calls):
        

cust1=Customer(9900009901,'cust1',23)
cust2=Customer(9900009902,'cust2',24)
cust3=Customer(9900009903,'cust3',25)

list_of_customers=[cust1,cust2,cust3]

call1=CallDetail(9900009901,8800123401,5,'Local')
call2=CallDetail(9900009903,8800123402,10,'STD')
call3=CallDetail(9900009902,8800123403,2,'STD')
call4=CallDetail(9900009901,8800123404,8,'ISD')
call5=CallDetail(9900009901,8800123405,7,'STD')
call6=CallDetail(9900009903,8800123406,9,'Local')
call7=CallDetail(9900009903,8800123407,4,'Local')

list_of_calls=[call1,call2,call3,call4,call5,call6,call7]
Util.parse_customer(list_of_customers, list_of_calls)
