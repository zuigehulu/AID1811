str1 = input("请输入一段字符串")
d ={}
for x in str1:
    # if x not in d:
    #     d[x]=1
    # else:
    #     d[x]=d[x] +1
    d[x] = str1.count(x)
print(d)
for x in d.items():
    # print(x,':',y,'次')
    print("%s:%s次"%x)
