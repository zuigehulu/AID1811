# closure.py
# 全局变量money不安全

money = 1000  # 父母的压岁

def child_buy(obj, m):
    global money
    if money > m:
        money -= m
        print('买', obj, '花了', m, '元', '剩余', money)
    else:
        print("买", obj, '失败')

child_buy('变形金刚', 200)
money = 0  # 钱被偷了
child_buy('漫画三国', 100)
child_buy('手机', 1300)



