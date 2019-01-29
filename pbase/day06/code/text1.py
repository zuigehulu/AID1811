# 输入一个开始的整数，用begin绑定
# 输入一个结束的整数，用end绑定
# 将从begin开始，到end结束（不包括end）的偶数存在于列表中
# 建议用列表推到实现
begin = int(input("输入一个开始的整数"))
end = int(input("输入一个结束的整数"))
L = [x for x in range(begin,end) if x % 2 == 0 ]
print(L)