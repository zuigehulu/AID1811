# class_method.py

# 此示例示意用类方法来访问类属性和改变类属性 
class A:
    v = 0  # 类属性

    @classmethod
    def get_v(cls):
        return cls.v

    @classmethod
    def set_v(cls, v):
        cls.v = v

# 类方法不能访问此类创建的对象的实例属性
a1 = A()  # 创建一个对象
a1.v = 9999  # 创建实例属性
a1.set_v(8888)
print(A.get_v())  # 8888