# 练习:
#   写一个学生类 Student类, 此类用于描述学生信息,学生信息有
#     姓名,年龄,成绩(默认为0)
#   1. 为该类添加初始化方法,实现在创建对象时自己自动设置,
#      姓名,年龄,成绩
#   2. 添加 set_score方法能力对象修改成绩信息
#   3. 添加show_info方法打印学生对象的信息
#   如 :
#     class Student:
#         def __init__(...):
#             ...
#         def set_score(...):
#             ...
#         def show_info(...):
#             ...
#     L = []
#     L.append(Student('小张', 20, 100))
#     L.append(Student('小李', 18, 98))
#     L.append(Student('小王', 19))
#     L[2].set_score(80)
#     for s in L:
#         s.show_info()  # 显示每个对象的信息



class Student:
    def __init__(self, n, a, s=0):
        self.name = n
        self.age = a
        self.score = s

    def set_score(self, s):
        self.score = s

    def show_info(self):
        print(self.name, '年龄', self.age,
              '岁,成绩是:', self.score)

L = []
L.append(Student('小张', 20, 100))
L.append(Student('小李', 18, 98))
L.append(Student('小王', 19))
L[2].set_score(80)
for s in L:
    s.show_info()  # 显示每个对象的信息

print(L)
