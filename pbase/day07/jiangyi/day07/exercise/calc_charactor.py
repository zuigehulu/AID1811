# 练习:
#   输入一段字符串, 打印出这个字符串出现过的字符及出现过的次数
#   如:
#     请输入:abcdabcaba
#   打印:
#     a: 4次
#     b: 3次
#     d: 1次
#     c: 2次
#     (注: 不要求打印次序)

s = input("请输入: ")
# 方法1
# d = {}
# for ch in s:
#     d[ch] = s.count(ch)


# 方法2
d = {}
for ch in s:
    if ch in d:  # 说明ch这个字符已经出现过
        d[ch] += 1
    else:  # ch这个字符是第一次出现
        d[ch] = 1

# print(d)
# 打印:
for t in d.items():
    print("%s: %d次" % t)  # 注: t 绑定元组


