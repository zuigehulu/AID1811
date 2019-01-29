L = [100,190,165,170,155,108,139,175,160,180]

def bubble(value):
    #外层循环对应走访数据的次数
    for i in range(len(value)-1):
    #内层循环对应走访数据对比的次数
        for j in range(len(value)-i-1):
            if value[j] > value[j+1]:
                value[j],value[j+1] = value[j+1],value[j]

bubble(L)
print(L)