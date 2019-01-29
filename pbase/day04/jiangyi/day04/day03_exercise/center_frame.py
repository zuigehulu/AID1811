#   3. 输入三行文字,让这三行文字在一个方框内居中显示
#     如(请不要输入中文):
#       请输入第1行: hello!
#       请输入第2行: I'm studing python!
#       请输入第3行: I like python!
#     打印如下:
#       +---------------------+
#       |       hello!        |
#       | I'm studing python! |
#       |   I like python!    |
#       +---------------------+



a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")

max_len = max(len(a), len(b), len(c))
print("最大长度是:", max_len)

line1 = '+-' + '-' * max_len + '-+'
# 打印最上边一行
print(line1)

# 打印中间的 三行
print('| ' + a.center(max_len) + ' |')
print('| ' + b.center(max_len) + ' |')
print('| ' + c.center(max_len) + ' |')
 
# 打印最下边一行 
print(line1)