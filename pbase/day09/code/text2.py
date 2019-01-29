# 写一个函数priem_m2n(m,n)返回从m开始，
# 到n结束范围内的素数，返回这些素数的列表并打印
def isprime(n):
    for x in range(2,n):
        if n%x == 0:
            return False
    return True

def prime_m2n(m,n):
    lst = []
    for x in range(m,n):
        if isprime(x) == True:
            lst.append(x)
    return lst

print(prime_m2n(10,20))
