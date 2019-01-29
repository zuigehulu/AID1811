#　定义装饰器函数，并装饰func
# 装饰求的原理是替换被装饰函数的变量绑定关系
#用装饰器语法实现方法见:mydeco3.py
def mydeco(fn):
    def fx():
        print("+++++++++")
        fn()
        print("---------")
    return fx

def myfunc():
    print("被调用")

myfunc = mydeco(myfunc)
myfunc()
myfunc()
myfunc()