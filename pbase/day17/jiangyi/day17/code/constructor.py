# myclass.py


# 定义一个新的类,此类来描述狗的行为和属性
class Dog:
    '''这是类的文档字符串
    此类用于描述一种动物的行为和属性
    '''
    pass

dog1 = Dog()  # 用Dog类来创建一个Dog类型的对象
print(id(dog1))
dog2 = Dog()  # 用构造函数来创建另一个Dog类型的对象
print(id(dog2))


lst1 = list()  # 用list类来创建一个列表对象
print(id(lst1))
lst2 = list()  # 创建另一个列表对象
print(id(lst2))
