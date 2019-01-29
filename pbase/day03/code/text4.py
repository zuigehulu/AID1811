# 3. 输入三行文字,让这三行文字在一个方框内居中显示
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
num1 = input("请输入第1行:")
num2 = input("请输入第2行:")
num3 = input("请输入第3行:")
print("+------------------------+")
print("|",num1.center(24),"|",sep="")
print("|",num2.center(24),"|",sep="")
print("|",num3.center(24),"|",sep="")
print("+------------------------+")

