#   2. 写一个程序,任意输入一个整数,判断这个数是否为素数prime
#     素数(也叫质数),是只能被1和自身整数的正整数
#     如:  2 3 5 7 11 13 17 19 ...
#     提示:
#       用排除法: 当判断x是否为素数时,只要让x分别除以
#        2, 3, 4, 5, 6 ... x-1,只要有一次被整除,则x不是
#        素数,否则x是素数

x = int(input('请输入一个整数: '))
if x < 2:
    print(x, '不是素数')
else:
    # 用一个变量Flag作为标志,很假设x是素数,Flag=True
    # 当不是素数时,把变量值改变False,最后由变量Flag的真假值
    # 来判断x是否为素数
    flag = True  # 先假设x为素数
    for i in range(2, x):  # i为2,3,4,.... x-1
        if x % i == 0:
            # print(x, '不是素数')
            flag = False
            break
    if flag:
        print(x, '是素数')
    else:
        print(x, '不是素数')

