L = [80,70,30,50,69,78,90,100,65,88]

def charu(L):
    l = [L[0]]
    for x in range(1,len(L)):
        #获取当前无序数据
        temp = L[x]
        pos = x
        for y in range(x-1,-1,-1):
            if L[y] > temp:
                L[y],L[y+1]=temp,L[y]
                #跟新插入取出数据的位置
                pos = j
            else:
                

        
               


charu(L)
print(L)