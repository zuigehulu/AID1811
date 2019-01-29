def mydeco(fn):
    '''这是一个装饰器
    fn是参数名字，也是需要装饰器器的函数名
    '''
    def fx():
        print("+++++++++")
        fn()
        print("---------")
    return fx

@mydeco  #和myfunc = mydeco(myfunc)作用一模一样
def myfunc():
    print("被调用")

myfunc()
