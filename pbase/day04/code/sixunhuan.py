n = ''
i = 1
d = 0
print("请输入一些整数，当输入负数时结束:")
while True:   
    a = int(input("请输入第%d个数"%i))
    i += 1
    if a < 0:
        break
    n = n +" "+ str(a)
    d += a
print("您输入的数是:%s,和是:%d"%(n,d))