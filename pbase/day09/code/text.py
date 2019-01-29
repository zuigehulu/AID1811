# 写一个函数isprime(x) 判断x是否是素数，
# 如果是则返回true，否则返回false
def isprime(n):
    for x in range(2,n):
        if n%x == 0:
            return False
    return True

print(isprime(17))
print(isprime(2))
print(isprime(98))

            
