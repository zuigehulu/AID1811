# 练习:
#   输入一个字符串,从尾向头输出这个字符串的字符
#     如:
#       请输入: hello
#     打印如下:
#       o
#       l
#       l
#       e
#       h

#   可以用 while语句 或 for语句 实现  

s = input("请输入: ")
# 用while语句实现
index = len(s) - 1
while index >= 0:
    ch = s[index]
    print(ch)
    index -= 1  # 让索引值前移


# 用 for语句 实现
print('----------以下用for语句实现--------------')
for ch in s[::-1]:
    print(ch)


