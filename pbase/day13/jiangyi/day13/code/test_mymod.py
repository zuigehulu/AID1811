# test_mymod.py

# 此程序示意导入mymod.py模块,并调用内部的函数,打印
# mymod.py内部的数据

import mymod  # 导入自定义模块(注意,不用加.py)

mymod.myfac(5)
mymod.mysum(100)
print(mymod.name1)  # audo

from mymod import name2
print("name2=", name2)  # tesla

from mymod import *
myfac(20)



