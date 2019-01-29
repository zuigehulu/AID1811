# 练习:
#   已知内建函数 max 的帮助文档是:
#     >>> help(max)
#     max(iterable)
#     max(arg1, arg2, *args)
#   仿造max写一个mymax函数,功能与max函数完全相同
#     (要求:不允许调用 max 函数)

#     print(mymax([6, 8, 5, 3]))  # 8
#     print(mymax(100, 200))      # 200
#     print(mymax(1, 2, 5, 9, 7)) # 9

def mymax(*args):
    # print("args=", args)
    # 判断实参是一个可迭代对象,还是多个数据
    if len(args) == 1:  # args里是一个可迭代对象
        # 如: args=([6, 8, 5, 3],)
        iterable = args[0]  # 把可迭代对象取出
        zuida = iterable[0]
        for x in iterable:  # 依次从第一个和zuida进行比较
            if x > zuida:
                zuida = x
        return zuida  # 返回最大值
    elif len(args) > 1:  # args里是两个或两个以上的数据
        # 如: args=(1, 2, 5, 9, 7)
        zuida = args[0]
        for x in args:  # 遍历所有实参
            if x > zuida:
                zuida = x
        return zuida

print(mymax([6, 8, 5, 3]))  # 8
print(mymax(100, 200))      # 200
print(mymax(1, 2, 5, 9, 7)) # 9

print(mymax())  # 可以运行?
