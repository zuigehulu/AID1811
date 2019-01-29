def func(**kwargs):
    print("关键字参数的个数是:",len(kwargs))
    print("kwargs:",kwargs)

func(name=123,age=35,address=567)
func(a=1,b=2,c=3,d='abc',e=[1,2,3])