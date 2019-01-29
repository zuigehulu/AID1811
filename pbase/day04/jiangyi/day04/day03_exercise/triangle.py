#   1. 用字符串 * 运算符 打印三角形
#     要求输入一个数, 此整数代表此三角形离左侧的字符个数
#     如:
#       请输入左侧的空格数: 3
#         *
#        ***
#       *****
#      *******

blank_count = int(input("请输入左侧的空格数: "))
blanks = ' ' * blank_count  # 得到一个blank_count个空格的字符串
print(blanks + "   *")
print(blanks + "  ***")
print(blanks + " *****")
print(blanks + "*******")
