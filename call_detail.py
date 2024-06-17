class CallDetail:
    def __init__(self, phoneno, called_no, duration, call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type

    def set_phoneno(self, phoneno):
        self.__phoneno=phoneno

    def set_called_no(self, called_no):
        self.__called_no=called_no
    
    def set_duration(self, duration):
        self.__duration=duration

    def set_call_type(self, call_type):
        self.__call_type=call_type

    def get_phoneno(self):
        return self.__phoneno

    def get_called_no(self):
        return self.__called_no

    def get_duration(self):
        return self.__duration

    def get_call_type(self):
        return self.__call_type

        


class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]

        for call in list_of_call_string:
            call_detail_list=call.split(",")
            a=CallDetail(call_detail_list[0],
                         call_detail_list[1],
                         call_detail_list[2],
                         call_detail_list[3])
            self.list_of_call_objects.append(a)

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)
