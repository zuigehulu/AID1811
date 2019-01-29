L = [100,190,165,170,155,108,139,175,160,180]
# L = [200,100, 108, 139, 155, 160, 165, 170, 175, 180, 190]
def bubble(value):
    #外层循环对应走访数据的次数
    for i in range(len(value)-1):
        #设置标志位
        flag = False
    #内层循环对应走访数据对比的次数
        for j in range(len(value)-i-1):
            if value[j] > value[j+1]:
                value[j],value[j+1] = value[j+1],value[j]
                #数据交换，标志为True
                flag = True
        #检查是否进行数据交换
        #若未发生数据交换，则证明剩余数据有序，无需进行下一次数据的走访
        if flag == False:
            return i
            break

i = bubble(L)
print(L)
print(i+1)