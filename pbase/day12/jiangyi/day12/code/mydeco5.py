# mydeco5.py

# 模拟银行业务需求，用装饰器来扩展新功能
# 银行: 存钱，取钱　

# --------- 以下由小钱写了一个装饰-----
def privileged_check(fn):
    '''权限验证功能的装饰器'''
    def fx(n, x):
        print("权限验证中.....")
        fn(n, x)
    return fx

def send_message(fn):
    '''实现业务操作完成后发送短消息的功能'''
    def fy(n, x):
        fn(n, x)  # 先操作，再发消息
        print("正在发短消息给:", n, '...')
    return fy


# -------- 以下是魏老师写的程序--------
@privileged_check
def savemoney(name, x):
    print(name, '存钱', x, '元')

@send_message
@privileged_check
def withdraw(name, x):
    print(name, '取钱', x, '元')

# -----以下是调用者小张写的程序---------
savemoney('小王', 200)
savemoney('小赵', 400)

withdraw('小李', 500)

