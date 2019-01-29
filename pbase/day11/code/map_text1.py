def pow2(x,y):
    print("%d ** %d"%(x,y),end = " ")
    return x**y
for x in map(pow2,range(1,10),range(9,0,-1)):
    print(x)

print(sum(map(lambda x,y:x**y,range(1,10),range(9,0,-1))))