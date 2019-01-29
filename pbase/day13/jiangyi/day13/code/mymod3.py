# mymod3.py

# 此示例示意模块的隐藏属性
# 隐藏属性不会被  from import *语句导入

def f():
    pass

def _f():
    pass

def __f():
    pass

name1 = 'aaa'
_name = 'bbb'


