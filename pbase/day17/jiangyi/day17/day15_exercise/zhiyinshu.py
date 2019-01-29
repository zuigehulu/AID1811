#   3. 分解质因数,输入一个正整数,分解质因数
#      如
#        输入: 90
#      打印
#        90 = 2*3*3*5
#     注: 质因数是指最小能被原数整数的素数(不包括1)

def get_all_yinshu(x):
    '''此方法用来获取一个数x,的所有因数.
    返回因数的列表,如: x = 90
    返回: [2, 3, 3, 5]
    '''
    L = []
    while x > 1:
        # 每次找一个质因数,然后加入到列表后,
        for i in range(2, x + 1):
            if x % i == 0:  # 找到质因数
                L.append(i)
                # 变量x的值,
                x = int(x // i)
                break
    return L

    # return [2, 3, 3, 5]


n = int(input("请输入: "))
L = get_all_yinshu(n)
print(n, '=', '*'.join((str(x) for x in L)))

