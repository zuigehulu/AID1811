def myfun1(a,b,c):
    print('a=',a,end =' ')
    print(b,end=' ')
    print('c=',c,end = ' ')
    print()

d ={'a':1,'b':2,'c':3}
myfun1(**d)
myfun1(c=d['a'],b=d['c'],a=d['b'])
myfun1(100,*[200,300])  #正确的
myfun1(*(100,200),300)  #正确
myfun1(*[100],*'ab')  #正确
myfun1(*[100],200,*[300])  #正确
myfun1(2,b=1,c=3)
