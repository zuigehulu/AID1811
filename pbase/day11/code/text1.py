# 已知有列表：
# L = [[3,5,8],10,[[13,14],15,18],20]
# 写一个函数print＿list(lst) 打印所有数字
# 写一改函数，返回这个列表中所有数字的和
# 2.次额除１－２０阶乘和
'''
        if type(lst[0]) is int:
            return d.append(lst[0])
        elif len(lst) > 1:
            print_list(lst[1:])
        lst = lst[0:len(lst)-1]
        if type(lst[0]) is not int:
            print_list(lst[0])
'''
L = [[3,5,8],10,[[13,14],15,18],20]
d = []
def print_list(lst): 
   # print(lst[0])
   # print(lst[0:len(lst)])
    print(len(lst))
    if type(lst[0:len(lst)]) is int:
        pass
   #   print(lst)
       
        
print_list(L)
print(d)
# for x in reversed(print_list(L)):
#     print(x,end = ' ')
print()