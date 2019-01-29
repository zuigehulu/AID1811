L1 = [1,2,3,4,5]
L2 = ['a','b','c']
L3 = [(x,y) for x in L1
        for y in L2]
print(L3)
