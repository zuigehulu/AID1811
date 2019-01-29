# test_platfrom.py

import sys

if sys.platform == 'linux':
    print("当前程序正在运行在linux上")
elif sys.platform == 'win32':
    print("当前程序正在运行在Windows 32 位平台")