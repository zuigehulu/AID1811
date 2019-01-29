#  4. 写一个程序
#    输入一个开始的整数用变量begin绑定
#    输入一个结束的整数用变量end绑定
#    打印从 begin 到 end(不包含end) 之间的每个整数,打印在
#    一行内
#    如:
#      请输入开始值: 8
#      请输入结束值: 20
#    打印:
#       8 9 10 11 12 13 14 .... 19

#   附加思考:
#     如何实现每5个打印在一行内,打印多行?


begin = int(input("请输入开始值: "))
end = int(input("请输入结束值: "))

print_count = 0  # 此变量用来记录打印数字的个数  

i = begin  # i代表当前要打印的一个数
while i < end:
    print(i, end=' ')
    print_count += 1  # 增1
    if print_count % 5 == 0:
        print()  # 换行

    i += 1
else:
    print()



