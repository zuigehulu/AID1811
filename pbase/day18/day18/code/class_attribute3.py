# class_attribute.py


class Human:
    '''此示例示意类属性'''
    count = 0  # 创建类属性(类变量)

# 类属性可以通过此类的对象的__class__属性间接访问
print(Human.count)  # 0
h1 = Human()
h1.__class__.count = 100  # 可以通过__class__属性访问类

print(Human.count)  # 100


