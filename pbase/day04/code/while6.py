num = int(input("请输入一个整数:"))
i = num
while i >= 1:
    if i == 1 or i == num:
        print("*"*num)
    else:
        print("*"+(num-2)*" "+"*")
    i -= 1