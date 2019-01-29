class Car:
    ''' 此类定义一个小汽车类 '''
    def __init__(self,c,b,m):
        self.color = c
        self.brand = b
        self.model = m
    def run(self,speed):
        print("%s%s%s正在以%s公里／小时的速度行驶"%(self.color,
              self.brand,self.model,speed))
a4 = Car('紫色','奥迪','A4')
a4.run(199)