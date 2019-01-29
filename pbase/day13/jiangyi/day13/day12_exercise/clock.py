#   1. 写一个程序,以电子时钟的格式打印时间:
#     格式为:
#       HH:MM:SS
#     如:
#       17:51:20
#     时间自动变化


import time

while True:
    t = time.localtime()
    # print("%02d:%02d:%02d" % (t[3], t[4], t[5]),
    #       end='\r')
    print("%02d:%02d:%02d" % t[3:6],
          end='\r')
    time.sleep(1)

