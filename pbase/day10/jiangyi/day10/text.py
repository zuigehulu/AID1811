# # 练习:
# #   写一个计算公式的解释执行器, 已知有如下一些函数 
# #     def myadd(x, y):
# #         return x + y
# #     def mysub(x, y):
# #         return x - y
# #     def mymul(x, y):
# #         return x * y
# #     ...
# #   另有一个函数get_func,有一个参数op 代表用给定的字符串
# #     def get_func(op):
# #         ...  # 此处要添加代码
# #     此函数在传入字符串"加" 或 '+' 时返回myadd 函数
# #     此函数在传入字符串"减" 或 '-' 时返回mysub 函数
# myadd = lambda x,y : x + y
# mysub = lambda x,y : x - y
# mynul = lambda x,y : x * y
# def get_func(op):
#     if op == '+' or  op == '加':
#         return myadd
#     if op == "-" or op == '减':
#         return mysub
#     if op =='*' or op == '乘':
#         return mynul

# print(get_func('+')(100,20))

# 练习:
#   1. 写一个lambda 表达式:
#      fx = lambda n: .....
#    此表达式创建一个函数,判断n这个数的2次方+1能否被5整除,
#    如果能整除返回True,否则返回 False.
#     如:
#        print(fx(3))   # True
#        print(fx(4))   # False
# fx = lambda x:  True if (x**2+1)%5 == 0 else False
# fx = lambda x : (x**2+1)%5 ==0
# print(fx(3))
# print(fx(4))

#   2. 写一个lambda 表达式来创建函数,此函数返回两个参数的最大值
#     def mymax(x, y):
#         ...
#     mymax = lambda .....
#     print(mymax(100, 200))      # 200
#     print(mymax("ABC", '123'))  # ABC
# count = 0
# def hello(x):
#     print("hello",x)
#     global count
#     count += 1

# while True:
#     x = input('name:')
#     hello(x)
#     if count == 3:
#         break
# 2. 写一个函数 mysum(x) 来计算:
#      1 + 2 + 3 + 4 + .... + x 的和,并返回
#      (要求: 不允许调用sum函数)
#      如:
#         print(mysum(100))  # 5050
# def mysum(x):
#     if x == 1:
#         return 1
#     sum =  myfac(x) + myfac(mysum(x-1))
#     return sum
# print(mysum(100))
# def mysum(x):
#     sum = 0
#     for y in range(x+1):
#         sum += y
#     return sum
# print(mysum(100))
# 写一个函数myfac(n) 来计算n!(n的阶乘)
#      n! = 1*2*3*4*...*n 
#      如:
#         print(myfac(5))  # 120
# def myfac(n):
#     if n == 1:
#         return 1
#     fac = n*myfac(n-1)
#     return fac

# print(mysum(5))