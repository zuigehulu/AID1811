#一个小球落下１００，算第１０次反弹多高，１０此后总路程
def luoxia(luo,n):
    sum = luo
    for x in range(1,n+1):
        sum += 2*(luo/2)
        luo = luo/2
    print(luo)
    print(sum)
luoxia(100,10)
