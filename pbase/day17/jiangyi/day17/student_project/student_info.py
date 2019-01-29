#   3. 改写之前的学生信息管理程序,添加如下四个功能:
#       | 5)  按学生成绩高~低显示学生信息 |
#       | 6)  按学生成绩低~高显示学生信息 |
#       | 7)  按学生年龄高~低显示学生信息 |
#       | 8)  按学生年龄低~高显示学生信息 |



def input_student():
    L = []   # 创建一个列表,准备放字典
    while True:
        n = input("请输入姓名: ")
        if n == '':  # if not n:
            break
        try:
            a = int(input("请输入年龄: "))
            s = int(input("请输入成绩: "))
        except ValueError:
            print("您的输入有错,请重新输入!!!")
            import time
            time.sleep(2)
            continue
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

def remove_student(L):
    name = input("请输入要删除学生的姓名: ")
    # 方法1
    # for d in L:
    #     if d['name'] == name:
    #         L.remove(d)
    #         print("删除成功")
    #         return
    for i in range(len(L)):  # i代表列表的索引
        d = L[i]
        if d['name'] == name:
            del L[i]
            print("删除成功")
            return
    print("删除失败")

def modify_student(L):
    name = input("请输入要修改成绩的学生姓名: ")
    for d in L:
        if d['name'] == name:
            score = int(input("请输入学生成绩:"))
            d['score'] = score
            print("修改成功!")
            return
    print("修改失败！")

def output_student_by_score_desc(L):
    def get_score(d):
        return d['score']
    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)

def output_student_by_score_asc(L):
    L2 = sorted(L, key=lambda d: d['score'])
    output_student(L2)

def output_student_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d['age'], reverse=True)
    output_student(L2)

def output_student_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d['age'])
    output_student(L2)

def read_from_file(filename='si.txt'):
    '''读取filenamem 内容,形成字典的列表返回 
    返回: [
          {'name': '张三', 'age': 20, 'score': 100},
          {'name': '李四', 'age': 21, 'score': 96},
          {'name': '小王', 'age': 22, 'score': 98},
          ]
    '''
    L = []
    try:
        fr = open(filename)
        while True:
            s = fr.readline() # '张三 20 100\n'
            if not s:
                break
            s2 = s.rstrip()  # '张三 20 100' 去掉右边的空白字符?
            n, a, s = s2.split()  # ['张三', '20', '100']
            a = int(a)
            s = int(s)  # 转为整数
            L.append(dict(name=n, age=a, score=s))

        fr.close()
        print("读取数据成功!!")
    except OSError:
        print("读取数据失败")
    return L

def save_to_file(L):
    try:
        fw = open("si.txt", 'w')
        for d in L:
            print(d['name'], d['age'], d['score'],
                  file=fw)
        fw.close()
        print("保存成功")
    except OSError:
        print("保存失败!")





