
# file : mymod.py

'''这是一个自定义的模块mymod

内部含有两个函数:
   myfac 和 mysum
还有两个数据
   name1 和 name2
'''


def myfac(n):
    print("正在计算", n, '的阶乘')

def mysum(n):
    print("正在计算1+2+3+...+%d 的和" % n)

name1 = "audi"
name2 = 'Tesal'

print("mymod 模块被加载")
print("mymod.__name__ 值为: ", __name__)

