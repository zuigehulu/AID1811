# 看懂下面的程序在做什么
def fx(f,x,y):
    print(f(x,y))
fx((lambda a,b:a+b),100,200)
fx((lambda a,b:a**b),3,4)