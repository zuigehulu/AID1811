class Dog:
    ''' 这是一个类的文档字符串
    此类用于描述一种动物的行为和属性
    '''
    def eat(self,food):
        print(id(self),"小狗正在吃",food)
    def paly(self,obj):
        print("小狗正在玩儿",obj)
    def sleep(self,hour):
        print("小狗睡了",hour,"小时")

dog1 = Dog() #用dog类来创建一个Ｄog类型的对象
dog1.eat("骨头")
dog1.sleep("1")
dog1.paly("球")
dog2 = Dog() #用构造函数来创建一个Ｄog类型的对象
dog2.eat("人")
dog2.paly("飞盘")
dog2.sleep("3")

