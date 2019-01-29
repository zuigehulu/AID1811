# return.py


# 此示例示意用return语句给函数调用者返回信息s
def say_hello2():
    print("hello aaa")
    print("hello bbb")
    return [1, 2, 3, 4]
    print("hello ccc")

v = say_hello2()
print("v =", v)

v2 = say_hello2()
print("v2=", v)

