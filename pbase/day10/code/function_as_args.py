def f1():
    print("f1函数被调用")
def f2():
    print("f2函数被调用")

def fx(fn):
    print(fn)
    fn()

fx(f1)
fx(print)