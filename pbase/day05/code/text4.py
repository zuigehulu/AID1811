# 4.算出100~999的水仙花数
for x in range(100,1000):
    baiwei = x // 100
    shiwei = x % 100 // 10
    gewei = x % 10
    if baiwei**3+shiwei**3+gewei **3 == x:
        print(x)