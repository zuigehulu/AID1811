def pow2(x,y):
    return x**y
sum1 = 0
for x in map(pow2,range(1,10),[2 for x in range(1,9)]):
    print(x,end = " ")
    sum1 += x
print()
print(sum1)

print(sum(map(lambda x:x**3,range(1,10))))
