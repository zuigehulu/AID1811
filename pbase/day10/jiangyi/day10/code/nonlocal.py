# nonlocal.py

v = 100
def f1():
    v = 200
    print("函数开始时: f1.v=", v)

    def f2():
        nonlocal v
        v = 300  # 想让外部的嵌套函数的v为300
        print("f2.v=", v)
    f2()

    print("函数结束时: f1.v=", v)  # 300

f1()
print("全局的v=", v)  # 100

