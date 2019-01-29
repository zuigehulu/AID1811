#   2. 输入一年中的月份 1~12, 输出这个月在哪儿个季度,
#      如果用户输入的是其它的数,则提示用户"您输错了"

# 此示例示意if语句的嵌套
month = int(input("请输月份: "))

if 1 <= month <= 12:
    print("正常的月份")
    if month <= 3:
        print("春季")
    elif month <= 6:
        print("夏季")
    elif month <= 9:
        print("秋季")
    else:
        print("冬季")
else:
    print("您输错了")

