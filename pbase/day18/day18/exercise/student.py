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
    __slots__ = ['name', 'age', 'score']
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

infos = []  #  python 1班
infos2 = []  # python 2班 
def add_student(infos, n, a, s):
    '''添加一个学生信息'''
    stu = Student(n, a, s)
    infos.append(stu)

def del_student(infos):
    n = input("请输入要删除学生的姓名: ")
    for index, stu in enumerate(infos):
        if stu.name == n:
            del infos[index]
            print("删除", n, '成功!')
            return
    print("删除", n, '失败!')

def get_count(infos):
    return len(infos)

def get_avg_score(infos):
    s = 0
    for stu in infos:
        s += stu.score
    return s / get_count(infos)


add_student(infos, '小张', 20, 100)
add_student(infos, '小李', 18, 98)
add_student(infos, '小赵', 19, 99)
add_student(infos, '小王', 19, 89)
del_student(infos)
print(get_count(infos))
print("平均成绩是", get_avg_score(infos))


add_student(infos2, '小钱', 18, 99)
