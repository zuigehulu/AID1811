a = input("请输入四个数字:")+" "
i = 0
b = 0
d = len(a)
while i < d:
    if a[i] == ' ':
        c = ""
        while b<= i:
            c = str(c)+str(a[b]) 
            b = b+1  
        c = int(c)
        print(c)
    i = i+1