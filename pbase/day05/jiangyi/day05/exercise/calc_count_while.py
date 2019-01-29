#   1. 任意输入一段字符串,写程序做如下两件事:
#     1) 计算出空格的个数,并打印个数
#         (要求用for语句,不允许使用S.count方法)
#     2) 计算出字符串中全部英文字符的个数
#        (注:英文字符的编码值为0~127,可用ord(x) 函数进行判断)

#   2. 完成上题后思考,上述功能能否用while语句实现

s = input('请输入一段字符串: ')

blank_count = 0  # 用来记录空格的个数
index = 0  # index 表示当前字符的索引值
while index < len(s):  # 当索引没有越界时用索引用一个字符
    ch = s[index]
    if ch == ' ':
        blank_count += 1
    index += 1  # 让索引值增加1,用来下次取字符
# for ch in s:
#     if ch == ' ':
#         blank_count += 1

print("空格的个数是:", blank_count)

english_count = 0  # 用来记录英文字符的个数
index = 0
while index < len(s):
    ch = s[index]
    if 0 <= ord(ch) <= 127:
        english_count += 1
    index += 1

print("英文字符的个数是:", english_count)

