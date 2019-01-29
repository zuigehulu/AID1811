# 练习:
#   输入三行文字,让这三行文字依次以20个字符的宽度右对齐输出
#   如:
#     请输入第1行: hello world
#     请输入第2行: abcd
#     请输入第3行: a
#   输出结果为:
#             hello world
#                    abcd
#                       a
#   做完上面的题后再思考:
#     能否以最长的字符串长度进行右对齐显示(左侧填充空格)

a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")

max_length = len(a)
if len(b) > max_length:
    max_length = len(b)

if len(c) > max_length:
    max_length = len(c)

# 方法1
# print(' ' * (max_length-len(a)) + a)
# print(' ' * (max_length-len(b)) + b)
# print(' ' * (max_length-len(c)) + c)

# 方法2
fmt = '%' + str(max_length) + 's'  # '%8s'
print(fmt % a)
print(fmt % b)
print(fmt % c)


# print("%20s" % a)
# print("%20s" % b)
# print("%20s" % c)


