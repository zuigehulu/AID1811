def myfun1(a,b,c):
    print(a)
    print(b)
    print(c)

L = [1,2,3]
myfun1(L[0],L[1],L[2])
myfun1(*L)
t = (100,200,300)
myfun1(*t)
S = "abc"
myfun1(*S)