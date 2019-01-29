import math
class Human:
    count = 0 #创建类变量
    pass

print(Human.count) #获取类变量绑定的值
Human.count = 100  #修改类属性
print(Human.count)
h1 = Human()
print(h1.count)  #访问类属性，而不是实例属性
h1.count = 0  #创建实例属性而不是类属性
print(h1.count)  #优先访问实例属性当实例属性不存在时才会访问类属性
print(Human.count)
h1.__class__.count = 1000
#通过h1的__class__属性绑定的是类，然后修改类里面的变量
print(Human.count)
print(math.pi)