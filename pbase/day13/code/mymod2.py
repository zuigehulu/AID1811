#注:此all列表限定在from mymod2 import *时
#只导入f1和name1,其他会忽略
__all__ = ["f1",'name1']

def f1():
    pass
def f2():
    pass
name1 = '   asd'
name2 = "sd"