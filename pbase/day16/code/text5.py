# 三、有名为user_info.txt的文件，其内容格式如下，写一个程序，
# 删除id为100003的行；将id为100002的用户名修改为alex li；

# pizza,100001
# alex, 100002
# egon, 100003
L = []
try:
    fr = open("./pbase/day16/code/user_info.txt")
    while True:
        s = fr.readline()
        if s == '':
            break
        s = s.strip()
        l = s.split(',')
        # print(l)
        d = {l[1]:l[0]}
        # print(d)
        L.append(d)
finally:
    fr.close()
for x in L:
    if '100003' in x.keys():
        L.remove(x)  
        print("删除成功")
    if '100002' in x.keys():
        x['100002'] = 'alex li'
        print("修改成功")
print(L)
fw = open('./pbase/day16/code/user_info.txt','wt')
for x in L:
    for y in x.items():
        l = list(y)
        # print(l)
        fw.write(l[1])
        fw.write(',')
        fw.write(l[0])
        fw.write('\n')
fw.close()
