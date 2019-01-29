#   3. 项目(学生信息管理)
#     输入任意个学生的信息,形成字典后存入列表中
#        学生信息有: 姓名,年龄,成绩
#     如:
#       请输入姓名: tarena
#       请输入年龄: 15
#       请输入成绩: 99
#       请输入姓名: name2
#       请输入年龄: 20
#       请输入成绩: 80
#       请输入姓名: <回车> 结束输入
#     形成内部存储格式如下:
#     infos = [{'name': 'tarena', 'age':15, 'score':99},
#              {'name': 'name2', 'age':20, 'score':80}]
    
#     第二步以表格方式打印上述列表的内容:
#     +---------------+----------+----------+
#     |    姓名        |    年龄  |    成绩   |
#     +---------------+----------+----------+
#     |    tarena     |    15    |    99    |
#     |     name2     |    20    |    80    |
#     +---------------+----------+----------+


infos = []   # 创建一个列表,准备放字典
while True:
    n = input("请输入姓名: ")
    if n == '':  # if not n:
        break
    a = int(input("请输入年龄: "))
    s = int(input("请输入成绩: "))
    d = {}  # 每次创建一个
    d['name'] = n
    d['age'] = a
    d['score'] = s
    infos.append(d)

print(infos)

print("+---------------+----------+----------+")
print("|    姓名       |   年龄   |   成绩   |")
print("+---------------+----------+----------+")
for d in infos:
    sn = d['name']
    sa = str(d['age'])  # 转为字符串,容易居中
    ss = str(d['score'])
    print("|%s|%s|%s|" % (sn.center(15), 
                          sa.center(10),
                          ss.center(10)))


# print("|    tarena     |    15    |    99    |")
# print("|     name2     |    20    |    80    |")
print("+---------------+----------+----------+")