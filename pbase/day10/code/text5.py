import os
L = []
#　输入学生的信息，包括姓名，年龄，成绩
def input_student():
    qingping()
    while True:
        name = input("输入名字:")
        age = input("输入年龄:")
        scire = input("输入成绩:")
        d={"name":name,"age":age,"scire":scire}
        L.append(d)
        # print(L)
        panduan = input("是否继续（w:继续，q：退出）")
        if panduan == 'q':
            break

# 显示录入的学生信息
def output_student():
    qingping()
    xianshi = []
    xianshi.append(("+"+"-"*(60)+"+"))
    print('|'+'姓名'.center(20)+"|"+
            "年龄".center(16)+"|"+
            "成绩".center(16)+"|")
    for ch in L:
        print("+"+"-"*(60)+"+")
        if ord(ch['name'][0]) >255:
            print("|"+ch['name'].center(22-len(ch['name'])),end = "")
        else:
            print("|"+ch['name'].center(22),end = "")     

        print("|"+ch['age'].center(18)+'|'+
            ch['scire'].center(18)+"|")
    print("+"+"-"*(60)+"+")
    fanhui()

#删除学生信息
def shanchu(xinxi): 
    qingping()  
    for x in L:
        for ch in x.values():
             if xinxi == ch:
                print('名字',x['name'],'年龄',x['age'],'成绩',x['scire'])
                shifou = input("是否删除(Ｙ／Ｎ)")
                if shifou == 'y':
                    L.remove(x)
                    return           
    else:
        print("抱歉,没有这个学生信息")

#查找学生信息
def chazhao(xinxi):   #查找学生信息
    for x in L:
        for ch in x.values():
            if xinxi == ch:
                print('名字',x['name'],'年龄',x['age'],'成绩',x['scire'])
                fanhui()
                return
    else:
         print("没有此学生信息")
    fanhui()

#清屏
def qingping():
    os.system('clear')

# 每次操作的返回函数
def fanhui():
    while True:
        s = input("是否返回(N/Y)")
        if s == 'y':
            return 

#主函数
def main():
    while True:
        qingping()
        print("1.添加学生信息")
        print("2.删除学生信息")
        print("3.查找学生信息")
        print("4.显示全部信息")
        print("5.退出(q)")
        num = input("请进行操作:")
        if num == '1':   #添加操作
            input_student()
        elif num == '2': #删除操作
            xinxi = input("请输入学生名字:")
            shanchu(xinxi)
        elif num == '3':        #查找操作
            xinxi = input("请输入学生名字:")
            chazhao(xinxi)
        elif num == 'q':
            return
        elif num == "4":
            output_student()
main()