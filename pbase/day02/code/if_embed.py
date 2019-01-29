month = int(input("请输入月份:"))

if 1 <= month <= 12:
    print("这是月份")
    if month <= 3:
        print("春季")
    elif month <= 6:
        print("夏季")
    elif month <= 9:
        print("秋季")
    elif month <= 12:
        print("冬季")
else:
    print("输入错误")
