class course:
    def __init__(self,string):
        self.Name=string
        self.students=[]
    def  add_stud(self,student):
        self.students.append(student)
    def stud_count(self):
        return len(self.students)
        


c1=course("Sunil")
c1.add_stud("student1")
c1.add_stud("student2")
c2=course("Patrick")
print(c1.Name)
print(c1.students)
x=c1.stud_count()
print(x)
#print(c2.Name)