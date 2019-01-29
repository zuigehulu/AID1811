money = 1000

def child_buy(obj,m):
    global money
    if money > m:
        print("买",obj,'花了',m,'元')
        money -= m
    else:
        print('买',obj,'失败')

child_buy('变形金刚',200)
child_buy("漫画三国",100)
child_buy('手机',1300)
    
    