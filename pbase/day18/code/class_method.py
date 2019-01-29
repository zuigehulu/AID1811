#此示例示意用类方法来访问类变量和改变类变量
class A:
    v = 0

    @classmethod
    def get_v(cls):
        return cls.v
    # #  def get_v(A,v)
    #    return A(v)
    @classmethod
    def set_v(cls,v):
        cls.v = v

print(A.v)
print(A.get_v()) #A.get_v(A.__class__)

A.set_v(80)
print(A.get_v())

a = A()
print(a.get_v())  # a.get_v(__class__)
a.set_v(100)
print(a.get_v())
