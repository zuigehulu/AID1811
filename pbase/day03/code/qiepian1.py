a = input("请输入一个字符串:\n")
b = len(a)//2
if a[:] == a[::-1]:
    print("这是回文") 

if len(a)%2 == 0 and a[:b] == a[:b-1:-1]:
    print("这是回文") 
elif len(a)%2 != 0:
    if a[:b] == a[:b:-1]:
        print("这是回文") 

