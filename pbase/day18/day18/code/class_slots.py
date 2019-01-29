# class_slots.py

class Human:
    # 此__slots__列表限定Human类型的对象只能用一个age属性
    __slots__ = ['age', 'name']
    def __init__(self, age):
        self.age = age
    def show_info(self):
        # if self.age > 140 or self.age < 0:
        #     print("haha")
        print('年龄是:', self.age)

h1 = Human(10)
h1.show_info()  # 10
# h1.Age = 11  # 报错!!!
h1.age = 200  #  
h1.show_info()  # 200