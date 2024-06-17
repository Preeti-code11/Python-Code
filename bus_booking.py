class Ticket:
    counter=0

    def __init__(self, passenger_name, source, destination):
        self.__passenger_name=passenger_name
        self.__source=source
        self.__destination=destination
        Ticket.counter+=1

    def set_passenger_name(self, passenger_name):
        self.__passenger_name=passenger_name

    def set_source(self, source):
        self.__source=source
    
    def set_destination(self, destination):
        self.__destination=destination

    #def set_ticket_id(self):
    #    self.__ticket_id=[]

    #def get_ticket_id(self):
    #    return self.__ticket_id

    def get_passenger_name(self):
        return self.__passenger_name

    def get_source(Self):
        return self.__source

    def get_destination(self):
        return self.__destination

    def validate_source_destination(self):
        if self.__source=="Delhi":
            if self.__destination=="Mumbai" or "Pune" or "Chennai" or "Kolkata":
                return True
            else:
                return False
        else:
            return False

    def generate_ticket(self):
        if self.validate_source_destination():
            l1=["00","01","02","03","04","05","06","07","08","09","10"]
            if Ticket.counter>10:
                l1.append(str(Ticket.counter))
            for index in range(0,Ticket.counter):
                self.__ticket_id="D"+self.__destination[0]+l1[index]
            print(self.__ticket_id)
            


t1=Ticket("Preeti","Delhi","Mysore")
t1.set_passenger_name("Preeti")
t1.set_source("Delhi")
t1.set_destination("Mysore")
t1.validate_source_destination()
t1.generate_ticket()


t2=Ticket("Akshit","Delhi","Mumbai")
t2.set_passenger_name("Akshit")
t2.set_source("Delhi")
t2.set_destination("Mumbai")
t2.validate_source_destination()
t2.generate_ticket()

t3=Ticket("Akshit","Delhi","Chennai")
t3.set_passenger_name("Akshit")
t3.set_source("Delhi")
t3.set_destination("Chennai")
t3.validate_source_destination()
t3.generate_ticket()

t4=Ticket("Akshit","Delhi","Mumbai")
t4.set_passenger_name("Akshit")
t4.set_source("Delhi")
t4.set_destination("Mumbai")
t4.validate_source_destination()
t4.generate_ticket()

t5=Ticket("Akshit","Delhi","Mumbai")
t5.set_passenger_name("Akshit")
t5.set_source("Delhi")
t5.set_destination("Mumbai")
t5.validate_source_destination()
t5.generate_ticket()

t6=Ticket("Akshit","Delhi","Mumbai")
t6.set_passenger_name("Akshit")
t6.set_source("Delhi")
t6.set_destination("Mumbai")
t6.validate_source_destination()
t6.generate_ticket()

t7=Ticket("Akshit","Delhi","Mumbai")
t7.set_passenger_name("Akshit")
t7.set_source("Delhi")
t7.set_destination("Mumbai")
t7.validate_source_destination()
t7.generate_ticket()

t8=Ticket("Akshit","Delhi","Mumbai")
t8.set_passenger_name("Akshit")
t8.set_source("Delhi")
t8.set_destination("Mumbai")
t8.validate_source_destination()
t8.generate_ticket()

t9=Ticket("Akshit","Delhi","Mumbai")
t9.set_passenger_name("Akshit")
t9.set_source("Delhi")
t9.set_destination("Mumbai")
t9.validate_source_destination()
t9.generate_ticket()

t10=Ticket("Akshit","Delhi","Mumbai")
t10.set_passenger_name("Akshit")
t10.set_source("Delhi")
t10.set_destination("Mumbai")
t10.validate_source_destination()
t10.generate_ticket()

t11=Ticket("Akshit","Delhi","Mumbai")
t11.set_passenger_name("Akshit")
t11.set_source("Delhi")
t11.set_destination("Mumbai")
t11.validate_source_destination()
t11.generate_ticket()

t12=Ticket("Akshit","Delhi","Mumbai")
t12.set_passenger_name("Akshit")
t12.set_source("Delhi")
t12.set_destination("Mumbai")
t12.validate_source_destination()
t12.generate_ticket()


            