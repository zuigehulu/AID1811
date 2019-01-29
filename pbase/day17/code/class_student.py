class Student:
    def __init__(self,name,age=0,score=0):
        self.name = name
        self.age = age
        self.score = score
    def set_score(self,score):
        self.score = score
    def show_iffo(self):
        print("%s今年%s,成绩%s"%(self.name,
              self.age,self.score))
L = []
L.append(Student('小张',20,100))
L.append(Student("小李",19))
L[1].set_score(80)
for s in L:
    s.show_iffo()
    