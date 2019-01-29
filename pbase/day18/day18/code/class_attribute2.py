# class_attribute.py


class Human:
    '''此示例示意类属性'''
    count = 0  # 创建类属性(类变量)

# 类属性可以通过类的实例直接访问
h1 = Human()
print(h1.count)  # 访问类的属性(而不是实例属性)

h1.count = 100  # 创建实例属性(而不是修改类属性)
print(h1.count)#优先访问实例属性(当实例属性不存在时才访问类属性)
print(Human.count)  # 0



