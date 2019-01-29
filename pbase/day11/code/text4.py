# 1-20阶乘的和
def jiecheng(x):
    if x == 0:
        return 1
    return x * jiecheng(x-1)
print(sum(map(jiecheng,range(1,21))))