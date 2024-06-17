class Classroom:
    classroom_list=['c1','c3','c5','c7','c9']     
    @staticmethod
    def search_classroom(class_room):
        if class_room.lower() in Classroom.classroom_list:
            return "Found"
            print("Classroom is find in leftwing")
        else:
            return -1
            print("Classroom is not find")

C1=Classroom()
Classroom.search_classroom("c1")
