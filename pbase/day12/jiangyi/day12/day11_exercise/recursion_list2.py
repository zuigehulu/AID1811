#   1. 已知有列表：
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数 print_list(lst) 打印出所有的数字
#        如:
#          print_list(L)  # 打印 3 5 8 10 13 14
#     2) 写一个函数 sum_list(lst) 返回这个列表中所有数字的和
#        如:
#          print(sum_list(L))  # 106
#     注:
#       type(x) 函数可以返回一个对象的类型
#       如: type(20) is int  # True
#           type([1, 2, 3]) is list  # True


L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
def print_list(lst, newline=False):
    # 循环遍历列表中的每个元素
    for x in lst:
        # 如果是数字,则打印
        if type(x) is int:
            print(x, end=' ')
        # 如果是列表,则打印这个列表print_list
        else:
            print_list(x)
    if newline:
        print()  # 换行

print_list(L, True)  # 打印 3 5 8 10 13 14


def sum_list(lst):
    s = 0
    for x in lst:  # 遍历列表中所有的数据 
        if type(x) is int:  # x是整数,则加到s中
            s += x
        elif type(x) is list:  # x 是列表, 加列表的和
            s += sum_list(x)
    return s

print('和是', sum_list(L))  # 106

