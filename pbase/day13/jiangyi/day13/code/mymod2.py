# mymod2.py

# 注: 此__all__列表限制在 from mymod2 import * 时
# 只导入 f1 和 name1,其它会被忽略

__all__ = ['f1', 'name1']

def f1():
    f2()
    f3()

def f2():
    pass

def f3():
    pass

name1 = 'aaa'
name2 = 'bbb'
