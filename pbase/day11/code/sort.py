def abs1(x):
    return -abs(x)
L = [-2,1,3,5,-4,0]
L2 = sorted(L,key = abs1)
print(L2)