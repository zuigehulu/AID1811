
#   5. 实现有界面的学生信息管理程序
#     选择菜单如下:
#       请选择: 1
#     学生信息和存储方法与原程序相同: 用列表里包含来存信息
#     要求: 每个功能写一个函数与之相对应




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

def show_menu():
    print("+-----------------------------+")
    print("| 1) 添加学生信息             |")
    print("| 2) 显示学生信息             |")
    print("| 3) 删除学生信息             |")
    print("| 4) 修改学生成绩             |")
    print("| q) 退出                     |")
    print("+-----------------------------+")


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
        elif s == 'q':
            break

main()