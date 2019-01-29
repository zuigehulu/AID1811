from tkinter import *
root = Tk()
root.title('title')
root.geometry("600x400")
var = StringVar()
var.set("This is tk")
l = Label(root,textvariable = var ,
         bg = 'green',font = ('宋体',12),
         width = 12 , height = 10)
l.pack()
root.mainloop()