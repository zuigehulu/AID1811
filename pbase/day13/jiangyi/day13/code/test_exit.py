# test_exit.py

# 此示例示意用sys.exit函数直接退出当前程序
import sys

def myfunc():
    print("函数开始")
    sys.exit()
    print("函数结束")

myfunc()

print("程序结束")
