#   3. 用程序while语句生成如下字符串,并打印结果
#     1) 'ABCDE........XYZ'
#     2) 'AaBbCcDdEe......XxYyZz'
#    函数:
#       ord(x)  / chr(x)

# 算出大写字母
upper_string = ''  # 用于存储大写的字符
upper_lower_string = ''
code = 65  # code = ord('A')
while code < 65 + 26:  # while code <= ord('Z')
    upper_string += chr(code)  # 追加大写字母到upper_string

    # 在upper_lower_string后追加一个大写和一个小写字母
    upper_lower_string += chr(code) + chr(code+32)
    # print(chr(code))
    code += 1

print("大写字母为:", upper_string)
print("大小写字母混合显示为:", upper_lower_string)



