#   2. 编写一个闹钟程序,启动时设置定时时间,到时间后打印一句
#     '时间到!!!' 然后退出程序


def run_alarm(hour, minute):
    '''此函数用来等待时间,当时间到写设定时间相等时
    退出此函数'''
    import time
    while True:
        t = time.localtime()
        print("%02d:%02d:%02d" % t[3:6], end='\r')
        if t[3:5] == (hour, minute):
            return
        time.sleep(1)



h = int(input("请输入定时的小时: "))
m = int(input("请输入定时的分钟: "))

run_alarm(h, m)
print("时间到!!!")

