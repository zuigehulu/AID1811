str1 = input("任意输入一串字符:")
i = 0
j = 0
for ch in str1:
    if ch == " ":
       i +=1
    if 0<ord(ch)<123:
        j +=1
print("空格数是:",i)
print("英文字符是:",j)