# 如:请输入姓名:tarena
# 　请输入年龄：１５
# 　请输入成绩:98
# 形成存储格式:
# infos =[{'name':'tarena','age':15,'score':99}
# 　　　　　{'name':'xiaozhang','age':15,'score':99｝]

# 第二步，打印表格 
# +-------------------------------------+
# | 姓名   |      年龄 　 　｜　　成绩　　　｜
# +-------------------------------------+
# | tarena|    15         |    99       |
# +-------------------------------------+　　
L = []
#　输入学生的信息，包括姓名，年龄，成绩
def input_student():
    while True:
        name = input("输入名字:")
        age = input("输入年龄:")
        scire = input("输入成绩:")
        d={"name":name,"age":age,"scire":scire}
        L.append(d)
        # print(L)
        panduan = input("是否继续（w:继续，q：退出）")
        if panduan == 'w':
            continue
        elif panduan == 'q':
            break
# 显示录入的学生信息
def output_student():
    print("+"+"-"*(60)+"+")
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

# import sys

# if (sys.version_info > (3, 0)):
#     from tkinter import *
#     from tkinter import messagebox
# else:
#     from Tkinter import *

# student_bg_color = "#bbada0"

# mapcolor = {
#     '姓名':("#cdc1b4", "#776e65")
#     '年龄':("#eee4da", "#776e65")
#     '成绩':("#f65e3b", "#f9f6f2")
# }

# # 游戏各方块的lable数据
# map_labels = []

# #鼠标按下处理
# def on_mouse_down(event):
#     print("clicked at",event.x,event.y)

input_student()
from tkinter import *
root = Tk()   #初始化Ｔk()
root.title("label-test")  #设置窗口标题
root.geometry("1000x800")   #设置窗口的大小，注意是x不是＊
root.resizable(width=False,height=False)  #设置窗口的长宽是否可变，True为可变，默认为True
l = Label(root,text = output_student(),bg = "pink",font = ('宋体',12),width = 110,height = 30)
l.pack(side = RIGHT)  #这里的side可以赋值为LEFT RIGHT TOP BOTTOM
root.mainloop()  #进入消息循环
