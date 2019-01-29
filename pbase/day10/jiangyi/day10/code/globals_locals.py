# globals_locals.py

a = 1
b = 2
c = 3
def fn(c, d):
    e = 300
    # 能否在此处知道有哪儿些全局变量哪 些局部变量
    print("locals()返回:", locals())
    print("globals()返回:", globals())
    print(c)   # 100
    print(globals()['c'])    # 3
    # 等同于
    ddd = globals()
    print(ddd['c'])

fn(100, 200)

