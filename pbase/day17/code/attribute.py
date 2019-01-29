class Dog:
    def eat(self,food):
        print(self.color,'的',self.kinds,"正在吃",food)
        self.last_food = food
    def food_info(self):
        print(self.color,'的',self.kinds,'上次吃的是',self.last_food)
dog1 = Dog()
dog1.color = "白色" #为dog1对象添加color属性，绑定白色
dog1.kinds = '京巴'

# print(dog1.color,'的',dog1.kinds)
dog1.eat('骨头')
dog2 = Dog()
dog2.color = '灰色'
dog2.kinds = '哈士奇'
dog2.eat('狗粮')
dog1.food_info() #显示dog1上次吃的是什么
dog2.food_info() #显示dog2上次吃的是什么