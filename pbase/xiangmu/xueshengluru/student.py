# 1. 主事件循环的main函数放在 main.py 中
# 2. 显示菜单的函数show_menu 放在 menu.py 中
# 3. 与学生信息操作相关的函数放在student_info.py 中


#　输入学生的信息，包括姓名，年龄，成绩
def input_student(L):
    qingping()
    while True:
        name = input("输入名字:")
        age = int(input("输入年龄:"))
        scire = int(input("输入成绩:"))
        d={"name":name,"age":age,"scire":scire}
        L.append(d)
        # print(L)
        panduan = input("是否继续（w:继续，q：退出）")
        if panduan == 'q':
            break

# 显示录入的学生信息
def output_student(L1):
    xianshi = []
    xianshi.append(("+"+"-"*(60)+"+"))
    xianshi.append("|"+"学生信息管理系统".center(52)+"|")
    xianshi.append(("+"+"-"*(60)+"+"))
    xianshi.append(('|'+'姓名'.center(20)+"|"+
            "年龄".center(16)+"|"+
            "成绩".center(16)+"|"))
    for ch in L1:
        xianshi.append("+"+"-"*(60)+"+")
        if ord(ch['name'][0]) >255:
            xianshi.append(("|"+ch['name'].center(22-len(ch['name'])),"|"+ch['age'].center(18)+'|'+
            ch['scire'].center(18)+"|"))
        else:
            xianshi.append(("|"+ch['name'].center(22)+"|"+ch['age'].center(18)+'|'+
            ch['scire'].center(18)+"|"))     
    xianshi.append(("+"+"-"*(60)+"+"))
    xianshihanshu(xianshi)
    
#删除学生信息
def shanchu(xinxi,L): 
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
def chazhao(xinxi,L):   #查找学生信息
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
    import os
    os.system('clear')

# 每次操作的返回函数
def fanhui():
    while True:
        s = input("是否返回(N/Y)")
        if s == 'y':
            return 

#用于界面显示
from tkinter import *
def xianshihanshu(xianshi):
    root =Tk()
    root.title('学生信息管理系统')
    root.geometry("600x800") 
    var = StringVar()
    lb = Listbox(root,listvariable = var,
                bg = "#bbada0", font = ("宋体",12),
                width = 70,height = 20)
    list_items = xianshi
    for item in list_items:
        lb.insert('end',item)
    def guanbi(Event):
        b.config(command = jiemian)
    b = Button(root,text = '返回',width = 10 , height = 3,
                bg = 'red',font = ('宋体',15))
    list_items.clear()
    b.bind ('<ButtonRelease-1>',guanbi)
    b.pack(side = BOTTOM)
    lb.pack()   
    root.mainloop()
#添加界面
def jiemian():
        print("1.添加学生信息")
        print("2.删除学生信息")
        print("3.查找学生信息")
        print("4.显示全部信息")
        print("5.退出(q)")
#找到成绩的函数
#将列表按成绩从大到小排序
def paixu(bianliang,revs,L):
    L1 = sorted(L,key = lambda x : x[bianliang],reverse = revs)
    output_student(L1)
    
#将列表成绩按从小到大排序
def chengji_low(bianliang,L):
    L1 = L.copy()
    i = 0
    while i <len(L1):
        j = i
        while j < len(L1):
            if L1[i][bianliang] > L1[j][bianliang]:
                L1[i],L1[j] = L1[j],L1[i]
            j += 1
        i += 1
    output_student(L1)

#显示里的菜单
def xianshi_xueshengxinxi_jiemian(L):
    qingping()
    print("1.按成绩从大到小显示")
    print("2.按成绩从小到大显示")
    print("3.按年龄从大到小显示")
    print("4.按年龄从小到大显示")
    print("5.(q)返回主列表")
    jieshoupaixu = input("请进行操作:")
    if jieshoupaixu == "1":
        paixu('scire',True,L)         
    elif jieshoupaixu == "2":
        paixu('scire',False,L)         
    elif jieshoupaixu == "3":
        paixu('age',True,L)          
    elif jieshoupaixu == "4":
        paixu('age',False,L)         
    else:
        return

#主函数
def main():
    L = []
    while True:
        qingping()
        jiemian()
        num = input("请进行操作:")
        if num == '1':   #添加操作
            input_student(L)
        elif num == '2': #删除操作
            xinxi = input("请输入学生名字:")
            shanchu(xinxi,L)
        elif num == '3':        #查找操作
            xinxi = input("请输入学生名字:")
            chazhao(xinxi,L)
        elif num == 'q':
            return
        elif num == "4":  #显示学生全部信息
            xianshi_xueshengxinxi_jiemian(L)
main()