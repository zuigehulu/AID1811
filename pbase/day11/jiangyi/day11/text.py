# 练习:
#   1. 求 1**2 + 2**2 + 3**2 + ... + 9**2 的和
#   2. 求 1**3 + 2**3 + 3**3 + ... + 9**3 的和
#   3. 求 1**9 + 2**8 + 3**7 + ... + 9**1 的和
# s = sum(map(lambda x:x**2 ,range(1,10)))
# s1 = map(lambda x : x**3,range(1,10))
# s2 = map (pow,range(1,10),range(10,1,-1))
# print(s)
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(next(s1))
# print(s2)
# def sushu(n):
#     if n < 2:
#         return False
#     for x in range(2,n):
#         if n % x == 0:
#             return False
#     return True

# for x in filter(sushu,range(1,100)):
#     print(x)

#   以下列表的中的数据进行排序
# L = [(1, 5), (3, 9), (4, 1), (3, 6), (5, 3)]
#   1. 将列表内的五个元组按,第二个数据的从小到大的顺序进行排序
#     结果如下:
#     L = [(4, 1), (5, 3), (1, 5), (3, 6), (3, 9) ]
# def paixu(x):
#     return x[1]
# L1 = sorted(L,key = paixu)
# print(L1)
#   2. 将列表内的五个元组按第二个数的从大到小顺序进行排序,打印
#      排序之后的结果
# L2 = sorted(L,key = paixu ,reverse = True)
# print(L2)
#   3. 假设元组中的数据是数学直角坐标系的坐标,则按他们距离原点
#      的距离进行排序
#      (提示: 距离等同于 distance = sqrt(x**2 + y**2))
# from math import *
# def paixu2(n):
#     return sqrt(n[0]**2+n[1]**2)
# L3 = sorted(L,key = paixu2)
# print(L3)
def mai():
    qian = 1000
    def huaqian(x):
        nonlocal qian
        print("花了%d,还剩下%d"%(x,qian-x))
    return huaqian
s = mai()  #s = huaqian
s(100)   #huaqian(100)
s(200)
# qian = 1000
s(300)
# 1. 已知有列表：
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1) 写一个函数 print_list(lst) 打印出所有的数字
#        如:
#          print_list(L)  # 打印 3 5 8 10 13 14
#     2) 写一个函数 sum_list(lst) 返回这个列表中所有数字的和
#        如:
#          print(sum_list(L))  # 106
# L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
# def daying(L):
#     for x in L:
#         if type(x) is list:
#              daying(x)
#         else:
#             print(x)
# daying(L) 

# def sum1(L):
#     sum2 = 0
#     for x in L:
#         if type(x) is list:
#             sum2 += sum1(x)
#         else:
#             sum2 +=  x
#     return sum2
# print(sum1(L))

