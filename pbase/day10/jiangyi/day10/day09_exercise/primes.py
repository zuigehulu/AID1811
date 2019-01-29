#   1. 写一个函数 isprime(x) 判断x是否是素数,如果为素数则返回
#     True, 否则返回False

#   2. 写一个函数 prime_m2n(m, n) 返回从m开始,到n结束范围内
#     的素数(不包含n), 返回这些素数的列表,并打印
#     如:
#       L = prime_m2n(10, 20)
#       print(L)  # [11, 13, 17, 19]
#   3. 写一个函数primes(n), 返回指定范围内n(不包含n)的全部素
#      数的列表,并打印这些素数的列表
#       L = primes(10)
#       print(L)  # [2, 3, 5, 7]
#       1) 打印100 以内的全部素数
#       2) 打印 100 ~ 200之间全部素数的和

# 方法1
# def isprime(x):
#     if x < 2:
#         return False
#     # 能走到此处,x一定大于等于2
#     flag = True
#     for i in range(2, x):
#         if x % i == 0:  # x不是素数
#             flag = False
#             break
#     return flag

# 方法2
def isprime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:  # x不是素数
            return False
    return True


def prime_m2n(m, n):
    # 方法1
    # L = []
    # for x in range(m, n):
    #     if isprime(x):
    #         L.append(x)
    # return L
    # 方法2
    return [x for x in range(m, n) if isprime(x)]

L = prime_m2n(10, 20)
print(L)  # [11, 13, 17, 19]


def primes(n):
    return prime_m2n(0, n)

L = primes(10)
print(L)  # [2, 3, 5, 7]

# 1) 打印100 以内的全部素数
print(primes(100))
# 2) 打印 100 ~ 200之间全部素数的和
print(sum(prime_m2n(100, 200)))

