def f1():
    n = int(input("请输入整数:"))

def f2():
    try:
        f1()
    except ValueError as err:
        print("f1出错")
        print("f2的err=%s"%err)
        raise
try:
    f2()
except ValueError as err:
    print("f2内发生了错误,%s",err)