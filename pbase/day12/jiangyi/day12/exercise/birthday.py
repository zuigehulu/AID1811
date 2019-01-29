# 练习:
#   写一个程序，输入你的生日（年,月,日）
#     1) 算出你已经出生了多少天
#     2) 算出您出生那天是星期几?

import time

year = int(input("请输入您出生的年: "))
month = int(input("请输入您出生的月: "))
day = int(input("请输入您出生的日: "))
birth_tuple = (year, month, day, 0, 0, 0, 0, 0, 0)
# 计算出生时计算的内部时间秒数 
birth_second = time.mktime(birth_tuple)
# 再计算出生的时长(单位为秒)
life_second = time.time() - birth_second
life_days = life_second / 60 / 60 // 24
print("您已出生:", life_days, '天')
week = {
    0: '一',
    1: '二',
    2: '三',
    3: '四',
    4: '五',
    5: '六',
    6: '日',
}
# 得到出生时的时间元组
birth_tuple = time.localtime(birth_second)
print('您出生的那天是星期', week[birth_tuple[6]])


