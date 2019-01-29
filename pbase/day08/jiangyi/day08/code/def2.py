# def.py

g = 10  # 全局变量

# 此示例示意用def语句来创建一个函数
def say_hello():
    value = 100  # 在函数内部创建的变量叫局部变量
    print("hello world!")
    print("hello china!")
    print("hello tarena!")
    print("value=", value)  # 100
    print("外部的g = ", g)  # 10
    # g = 20  # 修改全局变量不合法

# 调用say_hello()
say_hello()
say_hello()
say_hello()
# print(value)  # 出错
print("g=", g)  # 10



