# 二、有名为username.txt的文件，其内容格式如下，写一个程序，
#  判断该文件中是否存在"alex", 如果没有，则将字符串"alex"添
#  加到该文件末尾，否则提示用户该用户已存在；
# pizza
# alex
# egon 
L = []
try:
    fr = open('./pbase/day16/code/username.txt','rt')
    while True:
        s = fr.readline()
        if s == '':
            break
        L.append(s.strip())
finally:
    fr.close()
for x in L:
    if x == 'alex':
        print("该用户已存在")
        break
else:
    L.append('alex')
try:
    fw = open('./pbase/day16/code/username.txt','wt')
    for x in L:
        fw.write(x)
        fw.write("\n")
finally:
    fw.close()

