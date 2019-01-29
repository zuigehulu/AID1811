# 有两个人：
# 　　　１．姓名　张三，年龄：３５
# 　　　２．姓名：李四，年龄：１５
# 行为：
# 　　１．　教别人学东西 teach
#     ２．　工作赚钱　　work
#     3.　借钱　　borrow（从xxx处借钱）
#     4.　显示自己的信息
# 事情:
#    1. 张三教李四学python
#    2.　李四教张三学王者荣耀
#    ３．张三上班赚钱１０００元
#    ４．李四向张三借钱　２００元
# 打印：　３５岁的张三有钱８００元，他学会的技能是：王者荣耀
# 　　　　１５岁的李四有钱２００元，他学会的技能是:python
class Human:
    
    def __init__(self,n,a,s=None,m=0):
        self.name = n
        self.age = a
        self.skill = []
        self.money = m
    
    def teach(self,other,s):
        print(self.name,'教',other.name,
             '学',s)
        other.skill.append(s)
    
    def borrow(self,other,m):
        print(self.name,"从",other.name,'借钱',m,'元')
        self.money = m
        other.money -= m
    
    def work(self,m):
        print(self.name,'上班赚钱',m,'元')
        self.money = m
    
    def show_xinxi(self):
        print("%s岁的%s有钱%s,他学会的技能是%s"%(self.age,self.name,self.money,self.skill))

zhangsan = Human('张三','35','python')
lisi = Human('李四',15,'王者荣耀')

# 李四教张三王者荣耀，张三教李四python
zhangsan.teach(lisi,'python')
lisi.teach(zhangsan,'王者荣耀')

#李四问张三借钱２００元，张三上班１０００元
zhangsan.work(1000)
lisi.borrow(zhangsan,200)

#输出
zhangsan.show_xinxi()
lisi.show_xinxi()

        
