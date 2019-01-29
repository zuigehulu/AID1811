str1 = input("请输入一个字符串:")
def xunzhao(str1):
    i = 0
    while i <len(str1):       
        if str1.count(str1[i]) == 1:
            return i
        else:
            i += 1
            continue
        i += 1
    return -1

str2 = xunzhao(str1)
print(str2)