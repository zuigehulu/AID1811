begin = int(input("请输入一个开始的整数:"))
end = int(input("请输入一个结束的整数:"))
i = 0
if begin <= end:
    while begin < end:
        print(begin,end = " ")
        begin += 1
        i += 1
        if i % 5 == 0:
            print()
    else:
        print()
else:
    while begin > end:
        print(begin,end = " ")
        begin -= 1
        i += 1
        if i % 5 == 0:
            print()
    else:
        print()