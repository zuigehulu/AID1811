#   4. 改写之前的学生信息管理程序,将程序 改为两个函数:
#       def input_student():
#           ....    # 此函数用于获取学生的信息,形成包含有字典的列表
#           然后返回此列表
#       def output_student(L):
#           ....   # 此函数以列格的形式打印学生信息的列表

#       测试(实现与之前相同的功能):
#       infos = input_student()
#       print(infos)
#       output_student(infos)


def input_student():
    L = []   # 创建一个列表,准备放字典
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
        L.append(d)
    return L

def output_student(L):
    print("+---------------+----------+----------+")
    print("|    姓名       |   年龄   |   成绩   |")
    print("+---------------+----------+----------+")
    for d in L:
        sn = d['name']
        sa = str(d['age'])  # 转为字符串,容易居中
        ss = str(d['score'])
        print("|%s|%s|%s|" % (sn.center(15), 
                            sa.center(10),
                            ss.center(10)))
    print("+---------------+----------+----------+")


infos = input_student()
print(infos)
output_student(infos)
