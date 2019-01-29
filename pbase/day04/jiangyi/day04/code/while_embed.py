
#   示例:
#     打印 1 ~ 20 的整数,打印在一行
#       1 2 3 4 5 .... 20
#     打印十行

j = 1
while j <= 10:
    # print('1 2 3 4 5 .... 20')
    i = 1
    while i <= 20:
        print(i, end=' ', flush=True)
        i += 1
    else:
        print()

    j += 1



