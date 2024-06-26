class University:
    def __init__(self):
        self.__student_id=None
        self.__marks=None
        self.__age=None

    def set_student_id(self,student_id):
        self.__student_id=student_id

    def set_marks(self,marks):
        self.__marks=marks

    def set_age(self,age):
        self.__age=age

    def get_student_id(self):
        return self.__student_id

    def get_marks(self):
        return self.__marks

    def get_age(self):
        return self.__age

    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False

    def validate_marks(self):
        if self.__marks in [0,101]:
            return True
        else:
            return False

    def check_qualification(self):
        if self.validate_age == True and self.validate_marks == True:
            if self.__marks>=65:
                return True
            else:
                return False
            
        else:
            return False


u1=University()
u1.set_student_id(1)
u1.set_age(23)
u1.set_marks(77)
u1.validate_age()
u1.validate_marks()
u1.check_qualification()
