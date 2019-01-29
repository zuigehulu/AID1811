# 写一个函数mysum(x)计算
def mysum(x):
    sum = 0
    for ch in range(1,x+1):
        sum += ch
    return sum
print(mysum(100))