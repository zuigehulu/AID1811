str1 = input("任意输入一串字符:")
i = " "
j = 0
a = 0
b = 0
while j < len(str1):
    if i == str1[j]:
        a += 1
    if 0 <= ord(str1[j]) < 128:
        b += 1
    j += 1

print(a)
print(b)