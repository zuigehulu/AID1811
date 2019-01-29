from tkinter import *
root = Tk()   #初始化Ｔk()
root.title("label-test")  #设置窗口标题
root.geometry("1000x800")   #设置窗口的大小，注意是x不是＊
root.resizable(width=False,height=False)  #设置窗口的长宽是否可变，True为可变，默认为True
l = Label(root,text='text',bg = 'pink',font = ('Arial',12),width=110,height=30)
# l1 = Label(root,text = "lable",bg = "pink",font = ('宋体',12))
# l2 = Label(root,text = "ＢＵＧ",bg = "pink",font = ('宋体',12),width = 8,height = 6)
l.pack(side = RIGHT)  #这里的side可以赋值为LEFT RIGHT TOP BOTTOM
# l2.pack()
# l1.pack(side = BOTTOM)
root.mainloop()  #进入消息循环
