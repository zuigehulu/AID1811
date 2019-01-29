import math
num =int(input('请输入一个整数:'))
zhuanhuan = ''
if num < 0:
    num = abs(num)
    zhuanhuan+='-'
n = int(math.log(num,7))
while n >= 0:
    i = 0
    while True:
        if num >= pow(7,n):
            num -= pow(7,n)
            i += 1
        else:
            break
    zhuanhuan +=str(i)
    n-=1
print(zhuanhuan)