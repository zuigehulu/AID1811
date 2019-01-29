# file : global3.py

# 4. global 变量列表里的变量名不能出现在函数的形参列表里.

v = 100
def fn(v):
    global v  # 报错!
    v = 200
    print(v)

fn(300)
print("全局的v=", v)