# 练习:
#   有两个人:
#     1. 姓名: 张三, 年龄: 35
#     2. 姓名: 李四, 年龄: 15
#   行为:
#     1. 教别人学东西 teach
#     2. 工作赚钱 work
#     3. 借钱 borrow(从xxx处错钱)
#     4. 显示自己的信息 show_info
#   事情:
#     张三 教 四李 学 python
#     李四 教 张三 学 王者荣耀
#     张三 上班赚钱 1000 元
#     李四 向 张三 错钱 200 元
#     35 岁的 张三 有钱 800 元,它学会的技能是: 王者荣耀
#     15 岁的 李四 有钱 200 元,它学会的技能是: python
#   如:
#     class Human:
#         def __init__(self, ....):
#             ...
#         def teach(self. ...)




#   行为:
#     1. 教别人学东西 teach
#     2. 工作赚钱 work
#     3. 借钱 borrow(从xxx处错钱)
#     4. 显示自己的信息 show_info
class Human:
    def __init__(self, n, a):
        self.name = n    # 姓名
        self.age = a     # 年龄
        self.money = 0   # 钱数
        self.skill = []  # 技能

    def teach(self, other, subject):
        print(self.name, '教', other.name,
              '学', subject)
        other.skill.append(subject)  # 结果

    def work(self, money):
        print(self.name, '上班赚钱', money, '元')
        self.money += money

    def borrow_from(self, other, money):
        print(self.name, '向', other.name, '借钱',
              money, '元')
        self.money += money
        other.money -= money

    def show_info(self):
        print(self.age, '岁的', self.name, '有钱',
              self.money, '元,它学会的技能是:',
              self.skill)

zhang3 = Human("张三", 35)
li4 = Human("李四", 15)
zhang3.teach(li4, 'Python')
li4.teach(zhang3, '王者荣耀')
zhang3.work(1000)
li4.borrow_from(zhang3, 200)

zhang3.show_info()
li4.show_info()

