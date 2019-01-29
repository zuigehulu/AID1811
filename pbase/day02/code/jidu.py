mon = int(input("请输入月份:"))

if mon == 1 or mon == 2 or mon == 3:
    print("这个月在第一季度")
elif mon == 4 or mon == 5 or mon == 6:
    print("这个月在第二季度")    
elif mon == 7 or mon == 8 or mon == 9:
    print("这个月在第三季度")
elif mon == 10 or mon == 12 or mon == 11:
    print("这个月在第四季度")
else:
    print("您输错了")

