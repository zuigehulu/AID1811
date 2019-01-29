a = input("请输入开始的字母:")
b = input("请输入结束的字母:")
c = ord(a)
e = ord(a)
d = ord(b)
# if 97 <= ord(a) <= 122:
#     e = ord(a) - 32
# else:
#     e = ord(a) + 32
if c <= ord('Z'):
    while c <= d:
        print(chr(c),end = " ")
        c += 1
    else:
        print()
else:
    while c <= d:
        print(chr(c-32),end = " ")
        c += 1
    else:
        print()

while e <= d:
    if e < 97:
        print(chr(e),end = "")
        print(chr(e+32),end = "")
    else:
        print(chr(e-32),end = "")
        print(chr(e),end = "")
    e += 1
else:
    print()


