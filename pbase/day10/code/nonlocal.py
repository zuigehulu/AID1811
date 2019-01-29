v = 100
def f1():
    global v
    v = 200
    print("函数开始时:f1.v=",v)
    def f2():
        nonlocal v 
        v = 300   #想让外部嵌套的v进行变化
        def f3():
            global v
            v = 400 
            print(v)           
        f3()
        print('v',v)
    f2()
    print("函数结束时:f1.v=",v)
f1()
print(v)