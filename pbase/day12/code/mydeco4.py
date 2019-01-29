#权限验证功能装饰器
def privileger_check(fn):
    def fx(n,x):
        fn(n,x)
        print('权限验证中')
    return fx
#发送短信装饰器
def send_message(fn):
    def fy(n,x):
        fn(n,x)
        print("发送消息给",n)
    return fy
#---------------------------------
@privileger_check
@send_message
def savemoney(name,x):
    print(name,'存入',x,'元')

@privileger_check
def withdmoney(name,x):
    print(name,"取钱",x,'元')
#-------------------------------------------
savemoney('小王',200)
print()
savemoney('小李',400)
print()
withdmoney('小赵',500)