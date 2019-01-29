# global.py


# 3. 不能先声明局部变量,再用global声明为全局变量,此做法不
#     符合规则v = 100

v = 100
def f1():
    v = 200  # 想让这条赋值语句改变全局的v
    global v  # 此处会报语法警告
    print(v)  # 200

f1()
print("v=", v)  # 200
