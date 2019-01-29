class ClassTest(object):
    __num = 0
    __student_class = []
    def __init__(self,num):
        ClassTest.__student_class = [x for x in range(1,num+1)]
    @classmethod
    def addNum(cls):
        cls.__num += 1

    @classmethod
    def getNum(cls):
        return cls.__num

    # 这里我用到魔术函数__new__，主要是为了在创建实例的时候调用人数累加的函数。
    # def __new__(self):
    #     ClassTest.addNum()
        # return super(ClassTest, self).__new__(self)


class Student(ClassTest):
    def __init__(self):
        self.name = ''
        ClassTest.addNum()
    # def __new__(self):
    #     return super(Student,self).__new__(self)
ClassTest(5)
a = Student()
b = Student()
print(ClassTest.getNum())