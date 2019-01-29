#   3. 写一个函数 input_number
#     def input_number():
#         ...  # 此处自己实现
#     此函数用来获取用户循环输入的整数.当输入负数时结束输入
#     将用户输入的数字形成列表的形式返回,再用内建函数max, min,
#     sum,求用户输入的最大值,最小值及和
#     L = input_number()
#     print("用户输入的最大值是:", max(L))
#     print("用户输入的最小值是:", min(L))
#     print("用户输入的全部数的和是:", sum(L))


# 方法1
# def input_number():
#     lst = []
#     while True:
#         x = int(input("请输入整数(小于零结束): "))
#         if x < 0:
#             break
#         lst.append(x)  # lst += [x]
#     return lst

# 方法2
def input_number():
    lst = []
    while True:
        x = int(input("请输入整数(小于零结束): "))
        if x < 0:
            return lst  #  return 执行时,此函数的所有语句都不再执行
        lst.append(x)  # lst += [x]



L = input_number()
print("用户输入的最大值是:", max(L))
print("用户输入的最小值是:", min(L))
print("用户输入的全部数的和是:", sum(L))
