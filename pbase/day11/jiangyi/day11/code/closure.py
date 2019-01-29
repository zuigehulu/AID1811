# closure.py
# 把money 变量放在外部嵌套函数作用域内

def give_yasui_money(m):
    money = m  # 创建一个外部嵌套函数的变量

    def child_buy(obj, m):
        nonlocal money
        if money > m:
            money -= m
            print('买', obj, '花了', m, '元', '剩余', money)
        else:
            print("买", obj, '失败')
    return child_buy

cb = give_yasui_money(1000)

cb('变形金刚', 200)
cb('漫画三国', 100)
cb('手机', 1300)



