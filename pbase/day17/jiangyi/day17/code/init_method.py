# init_method.py


class Car:
    '''此类定义一个小汽车类'''
    def __init__(self, c, b, m):
        self.color = c  # 颜色
        self.brand = b  # 品牌
        self.model = m  # 型号
        print("__init__初始化方法被调用!!!!")

    def run(self, speed):
        print(self.color, '的', self.brand,
              self.model,
              '正在以', speed, '公里/小时的速度行驶')

a4 = Car('红色', '奥迪', 'A4')
a4.run(199)

t1 = Car("蓝色", 'TESLA', 'Model S')
t1.run(230)



# t1.__init__('银色', 'Tesla', 'Model X')  # 显式调用初始化方法
# t1.run(240)

