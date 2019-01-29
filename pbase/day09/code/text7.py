def myfun1(a,b,c):
    print('收到',a,b,c)

print(myfun1(1,2,3))
l = [4,5,6]
print(myfun1(*l))
print(myfun1(a=7,b=8,c=9))
d ={'a':10,'b':11,'c':12}
print(myfun1(**d))