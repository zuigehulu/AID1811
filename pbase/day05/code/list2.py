i = 0
sum1 = 0
a = []
while True:
    b= int(input("请输入:"))
    if b < 0:
        break
    a += [b]
    sum1 += b
print(a)
print(sum1)