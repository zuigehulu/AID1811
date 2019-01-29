# 从键盘输入一段字符串，用变量s绑定
# １．将此字符传转为字节串用变量B绑定，并打印此字节串
# ２．打印字符串s的长度和字节串B的长度
# ３．将字节串b再转换为字符串用变量s2绑定，判断s2和s是否相同

s = input("输入一串字符串")
len_s = len(s)
b = s.encode()
len_b = len(b)
s2 = b.decode()
print("字节串:",b)
print("字符串长度:",len_s)
print("字节串长度:",len_b)
print('s和s2是否相同:',s==s2)
