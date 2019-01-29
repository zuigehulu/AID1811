str1 = input("请输入一个字符串:")
def xunzhao(str1):
    i = 0
    while True:
        s = str1[i]
        d = str1[i+1:]
        if i+1 == len(str1):
            return -1
        if s not in d:
            return i
        else:
            i += 1

str2 = xunzhao(str1)
print(str2)