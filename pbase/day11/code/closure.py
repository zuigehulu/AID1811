# money = 1000
def give_yasui_money(m):
    money = m
    def child_buy(obj,m):
        nonlocal money
        if money > m:
            print("买",obj,'花了',m,'元','还剩',money-m)
            money -= m
        else:
            print('买',obj,'失败')
    return child_buy
cb = give_yasui_money(1000)

cb('变形金刚',200)
cb("漫画三国",100)
cb('手机',1300)
    
    