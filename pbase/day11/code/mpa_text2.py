def pow2(x,y=2):
    return x**y
sum1 = 0
for x in map(pow2,range(1,10)):
    print(x,end = " ")
    sum1 += x
print()
print(sum1)