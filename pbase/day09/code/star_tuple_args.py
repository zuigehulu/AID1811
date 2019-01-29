def func(*args):
    print("实参个数是:",len(args))
    print('args=',args)

func()
func(1,2,3,4)
func(1,2,3,4,'aaa','BBB')