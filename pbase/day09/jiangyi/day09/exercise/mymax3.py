# 练习:
#   已知内建函数 max 的帮助文档是:
#     >>> help(max)
#     max(iterable)
#     max(arg1, arg2, *args)
#   仿造max写一个mymax函数,功能与max函数完全相同
#     (要求:必须调用 max 函数)

#     print(mymax([6, 8, 5, 3]))  # 8
#     print(mymax(100, 200))      # 200
#     print(mymax(1, 2, 5, 9, 7)) # 9

def mymax(a, *args):
    # 判断实参a是否是一个可迭代对象
    if len(args) == 0:
        return max(a)
    elif len(args) > 0:
        return max(a, *args)  # 把args绑定的元组拆开再按位置传参
        # return max(a, max(args))

print(mymax([6, 8, 5, 3]))  # 8
print(mymax(100, 200))      # 200
print(mymax(1, 2, 5, 9, 7)) # 9

# print(mymax())  # 可以运行?
