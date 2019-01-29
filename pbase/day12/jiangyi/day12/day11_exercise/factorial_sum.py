#   2.  写程序求出1~20的阶乘的和
#      即:  1!+2!+3!+....+20!

def factorial(x):
    '''此函数返回x!'''
    if x == 0:
        return 1
    return x * factorial(x - 1)

s = sum(map(factorial, range(1, 21)))

print(s)


