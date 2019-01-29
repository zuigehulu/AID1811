def range1(a,b=0,c=1):
    if a < b:
        a,b = b,a
    for x in range(b,a):
        print(x)

range1(10)
range1(1,10)