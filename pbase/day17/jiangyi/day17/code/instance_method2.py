# myclass.py


# 定义一个新的类,此类来描述狗的行为和属性
class Dog:
    '''这是类的文档字符串
    此类用于描述一种动物的行为和属性
    '''
    def eat(self, food):
        print("ID为", id(self), "的小狗正在吃", food)
    

dog1 = Dog()  # 用Dog类来创建一个Dog类型的对象
dog1.eat("骨头")

dog2 = Dog()  # 用构造函数来创建另一个Dog类型的对象
dog2.eat('狗粮')

Dog.eat(dog2, '窝头')


# lst1 = list()
# lst1.append(10)
# lst1.eat("包子")
