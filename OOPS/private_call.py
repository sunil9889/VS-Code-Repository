
class course:
    def __init__(self,name):
        self.name=name
        self.students=[]

    def  add_stud(self,student):
        self.students.append(student)
        self.__write_student(student)

    def stud_count(self):
        return len(self.students)
    def __write_student(self,student):
        print("Welcome " + student)

c1=course("Sunil")
c1.add_stud("student1")
c1.add_stud("student2")
x=c1.stud_count()
print(x)

    