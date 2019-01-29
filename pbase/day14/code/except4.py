def f1():
    pass
    raise ValueError("我错了")
def f2():
    f1()
    pass
def f3():
    f2()
    pass
def f4():
    f3()
try:
    f4()
except ValueError as err:
    print(err)