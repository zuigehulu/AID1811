def get_chinese_char_count(s):
    num = 0
    for x in s:
        if int(0x4e00) <= ord(x) <= int(0x9fa5):
            num += 1
    return num
#中引文编码　0x4e00  0x9fa5
s = input("请输入中英文混合的字符串")
print("您输入的中文字符个数为:",get_chinese_char_count(s))