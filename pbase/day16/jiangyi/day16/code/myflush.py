# myflush.py



import time

f = open('myflush.txt', 'w')


f.write('A')
f.flush()  # 强制清空缓冲区!

while True:
    pass

f.close()
