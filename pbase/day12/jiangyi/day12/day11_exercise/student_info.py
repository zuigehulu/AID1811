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






def show_menu():
    print("+---------------------------------+")
    print("| 1)  添加学生信息                |")
    print("| 2)  显示学生信息                |")
    print("| 3)  删除学生信息                |")
    print("| 4)  修改学生成绩                |")
    print("| 5)  按学生成绩高~低显示学生信息 |")
    print("| 6)  按学生成绩低~高显示学生信息 |")
    print("| 7)  按学生年龄高~低显示学生信息 |")
    print("| 8)  按学生年龄低~高显示学生信息 |")
    print("| q)  退出                        |")
    print("+---------------------------------+")


def main():
    infos = [] 
    while True:
        show_menu()
        s = input("请选择: ")
        if s == '1':
            infos += input_student()
        elif s == '2':
            # 显示学生信息:
            output_student(infos)
        elif s == '3':
            remove_student(infos)
        elif s == '4':
            modify_student(infos)
        elif s == '5':
            output_student_by_score_desc(infos)  # 降序
        elif s == '6':
            output_student_by_score_asc(infos)  # 升序
        elif s == '7':
            output_student_by_age_desc(infos)  # 降序
        elif s == '8':
            output_student_by_age_asc(infos)  # 升序
        elif s == 'q':
            break

main()