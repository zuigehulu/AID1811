# 5. 写一个程序, 输入一个整数n,打印一个宽度和高度都为n个字符的
#   长方形.
#     如:
#       请输入: 4
#     打印如下:
#       ####
#       #  #
#       #  #
#       ####
#     如: 
#       请输入: 6
#     打印如下:
#       ######
#       #    #
#       #    #
#       #    #
#       #    #
#       ######


w = int(input("请输入: "))

# 打印最上一行
print("#" * w)

# 打印中间的 w-2行
i = 1
while i <= w -2:
    # 此处的代码将会执行w-2行
    print('#' + ' ' * (w - 2) + '#')
    i += 1

# 打印最下一行
if w >= 2:
    print("#" * w)
