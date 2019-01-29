# 定义一个新的类,此类来描述狗的行为和属性
class Dog:
    def paly(self):
        print(self.color,self.pinzhong,'正在玩球')
    def eat(self,food):
        print(self,"吃",food)
        self.last_food = food
    def __repr__(self):
        return '小狗'
    def info(self):
        print(self.color,'的',self.pinzhong,'正在吃',self.food,'她上次吃的是',self.last_food)

dog1 = Dog()
dog1.color = '白色'
dog1.pinzhong = '京巴'
dog1.food = '麻花'
dog1.paly()
dog1.eat('狗粮')
dog1.info()

dog2 = Dog()
dog2.color = '灰色'
dog2.pinzhong = '二哈'
dog2.food = '狗粮'

dog2.paly()
dog2.eat('骨头')
dog2.info()
