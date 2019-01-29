import sys
a = sys.argv
b = 123
print(a)
for x in a[1:]:
    print("这是用str函数转换的Ｘ%s"%x)
    print("这是用repr函数转换的Ｘ%r"%x)
print("%s"%a)
print("%r"%a)
print("%r"%b)
print("%s"%b)
