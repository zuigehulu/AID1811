# 练习:
#   用类来描述一个学生的信息(可以修改之前写的Student类)
#   如:
#     class Student:
#         ... # 此处自己实现
    
#     将这些学生对象存于列表中, 写函数或方法实现添加学生和
#     删除学生信息等操作
#       1. 打印学生的个数
#       2. 打印学生的平均成绩

class Student:
    infos = []  # 类属性
    __slots__ = ['name', 'age', 'score']
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

    @classmethod
    def add_student(cls, n, a, s):
        '''添加一个学生信息'''
        stu = Student(n, a, s)
        cls.infos.append(stu)

    @classmethod
    def del_student(cls):
        n = input("请输入要删除学生的姓名: ")
        for index, stu in enumerate(cls.infos):
            if stu.name == n:
                del cls.infos[index]
                print("删除", n, '成功!')
                return
        print("删除", n, '失败!')

    @classmethod
    def get_count(cls):
        return len(cls.infos)

    @classmethod
    def get_avg_score(cls):
        s = 0
        for stu in cls.infos:
            s += stu.score
        return s / cls.get_count()


Student.add_student('小张', 20, 100)
Student.add_student('小李', 18, 98)
Student.add_student('小赵', 19, 99)
Student.add_student('小王', 19, 89)
Student.del_student()
print(Student.get_count())
print("平均成绩是", Student.get_avg_score())


