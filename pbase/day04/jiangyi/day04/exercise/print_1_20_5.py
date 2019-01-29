#   2. 打印 1 ~ 20 的整数, 每五个数字打印一行,打印四行
#     如:
#       1 2 3 4 5
#       6 7 8 9 10
#       ...
#     提示:
#       可以将 if 语句嵌入到while语句中

i = 1
while i <= 20:
    print(i, end=' ', flush=True)  # print(i, sep=' ', end='\n', flush=False)
    if i == 5:
        print()  # 换行
    if i == 10:
        print()
    if i == 15:
        print()
    if i == 20:
        print()
    i += 1
else:
    print()  # 换行 print(sep=' ', end='\n', flush=False)
