# global.py


v = 100
def f1():
    global v  # 声明v为全局变量
    v = 200  # 想让这条赋值语句改变全局的v

f1()
print("v =", v)  # 200