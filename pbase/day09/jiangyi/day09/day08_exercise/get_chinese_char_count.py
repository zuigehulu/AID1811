#   1. 写一个函数 get_chinese_char_count ,此函数实现的功能是
#     给定一个字符串,返回这个字符串中中文字符的个数
#       def get_chinese_char_count(s):
#           ...  # 此处自己实现

#       s = input('请输入中英文字混合的字符串:')
#       print("您输入的中文字符的个数是:",
#             get_chinese_char_count(s))
#     注: 中文字符的编码范围是: 0x4E00 ~ 0x9FA5(包含)



def get_chinese_char_count(s):
    count = 0  # 用来记录个数
    for ch in s:
        if 0x4E00 <= ord(ch) <= 0x9FA5:  # 判断是否是中文字符
            count += 1
    return count

s = input('请输入中英文字混合的字符串:')

print("您输入的中文字符的个数是:",
      get_chinese_char_count(s))

#     注: 中文字符的编码范围是: 0x4E00 ~ 0x9FA5(包含)

