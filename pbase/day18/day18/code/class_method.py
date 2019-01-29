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

print(A.v)    # 0
print(A.get_v())  # 0

A.set_v(80)
print(A.get_v())  # 80
print(A.v)   # 80
