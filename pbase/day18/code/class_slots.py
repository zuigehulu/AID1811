class Human:
    #次__slots__列表限定Human类型的对象只能用一个age属性
    __slots__ = ['age','name','score']
    def __init__(self,age):
        self.age = age
    def show_info(self):
        print('年龄是:',self.age)

h1 = Human(10)
h1.show_info()
h1.age = 11
h1.show_info()