class Student_calss(object):
    ''' 创建一个班级类，存放班级的个数　总人数　和现创建的班级'''
    __num = 0
    __student_class = []
    __class_num = 0
    # 根据输入创建班级，如果班级不存在则加入新班级．
    def __init__(self,num):
        if num not in self.__class__.__student_class:
            Student_calss.__student_class.append(num)
            Student_calss.__class_num  += 1
        
    @classmethod
    def addNum(cls):
        cls.__num += 1
    
    def addnum1(self):
        Student_calss.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num
    
    @classmethod
    def classprint(cls):
        print('班级有:',cls.__class_num,"个,分别是%s"%cls.__student_class)
        
class Student(Student_calss):
    def __init__(self,num,name):
        super().__init__(num)
        self.name = name
        Student_calss.addnum1(self)
    


a = Student(1811,'Tom')
b = Student(1810,'Bob')
print('现在总计有学生:',Student_calss.getNum(),'个')
Student_calss.classprint()
