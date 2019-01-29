# myclass.py


# 定义一个新的类,此类来描述狗的行为和属性
class Dog:
    '''这是类的文档字符串
    此类用于描述一种动物的行为和属性
    '''
    def eat(self, food):
        print("小狗正在吃", food)
    
    def sleep(self, hour):
        print("小狗睡了", hour, '小时')

    def play(self, obj):
        print("小狗正在玩", obj)

dog1 = Dog()  # 用Dog类来创建一个Dog类型的对象
dog1.eat("骨头")
dog1.sleep(1)
dog1.play('球')

dog2 = Dog()  # 用构造函数来创建另一个Dog类型的对象
dog2.eat('狗粮')
dog2.play('飞盘')
dog2.sleep(3)


