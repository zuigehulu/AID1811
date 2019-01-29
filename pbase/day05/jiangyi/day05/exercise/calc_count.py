#   1. 任意输入一段字符串,写程序做如下两件事:
#     1) 计算出空格的个数,并打印个数
#         (要求用for语句,不允许使用S.count方法)
#     2) 计算出字符串中全部英文字符的个数
#        (注:英文字符的编码值为0~127,可用ord(x) 函数进行判断)

s = input('请输入一段字符串: ')

blank_count = 0  # 用来记录空格的个数
for ch in s:
    if ch == ' ':
        blank_count += 1

print("空格的个数是:", blank_count)

english_count = 0  # 用来记录英文字符的个数
for ch in s:
    if 0 <= ord(ch) <= 127:
        english_count += 1

print("英文字符的个数是:", english_count)

