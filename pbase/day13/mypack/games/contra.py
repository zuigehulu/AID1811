#file : mypack/games/contra.py
# from .tanks import *
from mypack.menu import show_menu
def play():
    print("正在玩儿魂斗罗！！！")
def gameover():
    ''' 此函数示意包的相对导入，在当前contra.py模块中
    导入上一级（mypack）的menu.py李的show_menu，然后调用
    '''
    print("游戏结束！！")
    import time
    # time.sleep(2)
    #绝对导入
    # from mypack.menu import show_menu
    show_menu()
    #相对导入
    
    show_menu()
print("魂斗罗模块被加载")
gameover()