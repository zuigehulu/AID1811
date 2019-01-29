
# file : mypack/games/contra.py
from ..menu import show_menu

def play():
    print("正在玩 魂斗罗 ...")

def gameover():
    '''此函数示意包的相对导入,在当前contra.py 模块中
    导入上一级(mypack)的menu.py里的show_menu,然后调用
    '''
    print("游戏结束!!!!")
    import time
    time.sleep(2)

    # 绝对导入
    
    # 相对导入
    # from ..menu import show_menu
    # 错误的导入
    # from ...mypack.menu import show_menu

    show_menu()


print("魂斗罗 模块被加载!!!")

gameover()
