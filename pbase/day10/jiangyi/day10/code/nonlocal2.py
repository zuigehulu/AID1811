# nonlocal.py

# 3. 当有两层或两层以上函数嵌套时,访问nonlocal变量只对
#     最近一层的变量进行操作
v = 100
def f1():
    v = 200
    print("函数开始时: f1.v=", v)

    def f2():
        v = 300  # 想让外部的嵌套函数的v为300
        def f3():
            nonlocal v
            v = 400
        f3()
        print("f2.v=", v)  # 400
    f2()
    print("函数结束时: f1.v=", v)  # 200

f1()
print("全局的v=", v)  # 100

