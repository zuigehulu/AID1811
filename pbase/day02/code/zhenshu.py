num = int(input("请输入一个数字:"))

if num >= 0:
    print("这个数字的绝对值是本身")
elif num < 0:
    num = -num
    print("这个数的绝对值是",num)