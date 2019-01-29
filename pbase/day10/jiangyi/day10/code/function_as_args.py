# function_as_args.py


# 
def f1():
    print("f1函数被调用")

def f2():
    print("f2函数被调用")

def fx(fn):
    print(fn)  # ???
    fn()  # ???

fx(f1)
fx(f2)
fx(print)
# fx(max)  # 出错 
print("程序结束")

