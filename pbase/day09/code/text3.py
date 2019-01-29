# 写一个函数primes(n),返回指定范围内（不包含N）的全部
# 素数列表，并打印这些列表
def isprime(n):
    if n <= 2:
        return False
    else:
        for x in range(2,n):
            if n%x == 0:
                return False
        return True

def prime_m2n(m,n=0): 
    lst = []
    if n < m:
        for x in range(m):
            if isprime(x) == True:
                lst.append(x)
    else:
        for x in range(m,n):
            if isprime(x) == True:
                lst.append(x)
    return lst

def sum3(lst):
    sum = 0
    for x in lst:
        sum += x

print(prime_m2n(100))
lst = prime_m2n(100,200)
print(sum(lst))