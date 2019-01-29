# 输入一个整数n
# 当拿到的是１下次读取就条１步，得到２
# 当拿到的是２下次读取就跳２步，得到４
# 以此类推
# 将得到的数字生成一个列表
# 打印列表和所有元素之和
num = int(input("输入一个整数"))
liebiao = []
sum1 = 0
x = 1
while True:
    bushu = int(input("请输入步数:"))
    x += bushu
    if x >= num:
        break
    print(x)
    liebiao += [x]
    sum1 += x
print(liebiao)
print(sum1)
