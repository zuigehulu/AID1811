def func1(a,b,*args,c=0,d=0):
    print(a,b,args,c,d)

func1(1,2,3,4)
func1(11,22,33,44,d=44,c=33)
