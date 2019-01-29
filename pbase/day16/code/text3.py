# 一、有名为poetry.txt的文件，其内容如下，请删除第三行；
# 昔人已乘黄鹤去，此地空余黄鹤楼。

# 黄鹤一去不复返，白云千载空悠悠。

# 晴川历历汉阳树，芳草萋萋鹦鹉洲。

# 日暮乡关何处是？烟波江上使人愁。
fr = open("./pbase/day16/code/poetry.txt",'rt')
L = []
while True:
    s = fr.readline()
    if s =='':
        break
    L.append(s)
fr.close()
fw = open("./pbase/day16/code/poetry.txt",'wt')
print(L)
for x in L:
    if x == '黄鹤一去不复返，白云千载空悠悠。\n':
        L.remove(x)
        print('删除')
fw.writelines(L)
fw.close()