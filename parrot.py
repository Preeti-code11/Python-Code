class Parrot:
    unique_number=7000
      
    def __init__(self, name, color):
        self.__name=name
        self.__color=color
        Parrot.unique_number+=1

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def display(self):
        print(self.__name)
        print(self.__color)
        print(Parrot.unique_number)

p1=Parrot("Peehu", "Green")
p1.display()