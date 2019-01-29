def myfun1(a,b,c):
   print(a,b,c)

d ={'a':1,'b':2,'c':3}
myfun1(**d)
myfun1(c=d['a'],b=d['c'],a=d['b'])
