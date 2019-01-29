# 写一个程序，以电子时钟的方式打印时间
# hh:mm:ss
# 编写一个闹钟程序,启动时设置定时时间,到时间后打印一句
#     '时间到!!!' 然后退出程序
import time
import os
def now_time_fun():
    now_time =time.localtime()
    print("%d:%d:%d"%(now_time[3],now_time[4],now_time[5])) 
def naozhong(n):
    for x in range(n):
        now_time_fun()
        time.sleep(1)
        os.system("clear")
    print("时间到！！！")
def shuru():
    naolin = input("请输入您要设定的闹钟(小时:分钟:秒钟):")
    naolin1 = naolin.split(':')
    riqi = time.localtime()
    naolin_yuanzu=(riqi[0],riqi[1],riqi[2],int(naolin1[0]),int(naolin1[1]),int(naolin1[2]),0,0,0)
    naolin_miao = time.mktime(naolin_yuanzu)
    xian_miao = time.time()
    miao = int(naolin_miao - xian_miao)
    naozhong(miao)
shuru()
