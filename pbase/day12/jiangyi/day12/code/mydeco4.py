# mydeco1.py

# 装饰器原理示意

# 定义装饰器函数,并装饰 myfunc
# 装饰器的原理是替换被装饰函数的变量绑定关系

def mydeco(fn):
    def fx():
        print('++++++++++++++')
        fn()
        print('--------------')
    return fx

@mydeco
def myfunc():
    print("myfunc被调用!!!")

# myfunc = mydeco(myfunc)

myfunc()
myfunc()
myfunc()
