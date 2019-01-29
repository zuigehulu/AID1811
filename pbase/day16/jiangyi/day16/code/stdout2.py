# stdout2.py 

import sys

f = open("myprint.txt", 'w')

print(1, 2, 3, 4, file=f)

f.close()

print("程序正常退出!!!")





