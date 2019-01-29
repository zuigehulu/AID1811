def gupiao(L):
    min_gu = min(L)
    min_suo = L.index(min_gu)
    max_gu = max(L[min_suo:])
    if min_suo == len(L)-1 and max_gu == min_suo:
        return 0
    else:
        return max_gu - min_gu
L1 = [7,1,5,3,6,4]
L2 = [7,6,4,3,1]
zuida1 = gupiao(L1)
zuida2 = gupiao(L2)
print('第一支股票:',zuida1)
print('第二支股票:',zuida2)
