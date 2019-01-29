from tkinter import *
window = Tk()
window.title("my wimdow")
window.geometry('500x300')
l =Label(window,text = 'this is tk',
        bg = 'green',font = ('宋体',
        12),width = 15 ,height = 2)
l.pack()
window.mainloop()