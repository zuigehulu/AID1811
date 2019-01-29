from tkinter import *
from student_class import *
#用于界面显示
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
        b.config(command = exit)
    b = Button(root,text = '返回',width = 10 , height = 3,
                bg = 'red',font = ('宋体',15))
    list_items.clear()
    b.bind ('<ButtonRelease-1>',guanbi)
    b.pack(side = BOTTOM)
    lb.pack()   
    root.mainloop()
