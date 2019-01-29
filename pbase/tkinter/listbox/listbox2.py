from tkinter import *

root =Tk()
root.title('学生系统')
root.geometry("600x800")
xianshi = []
xianshi.append(("+"+"-"*(60)+"+"))
xianshi.append(('|'+'姓名'.center(20)+"|"+
            "年龄".center(16)+"|"+
            "成绩".center(16)+"|"))
var = StringVar()
# var.set((11,22,33,44))
lb = Listbox(root,listvariable = var,bg ="green",
                width = 50,height = 20)
list_items = xianshi
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.insert(1,'second')
lb.pack()
on_hit = False
def sd():
    lb.config(bg = 'blue')
def hit_me(event):
    b.config(command = exit())
b = Button(root,text = '返回',width = 15 , height = 12)
b.bind('<ButtonRelease-1>',hit_me)
b.pack()

root.mainloop()
