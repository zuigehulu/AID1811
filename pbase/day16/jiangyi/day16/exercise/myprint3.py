#   print函数是如何实现的,能否自己写一个myprint函数来代替
#   print函数
#   (注:  sys.stdout)

import sys

def myprint(*args, sep=' ', end='\n',
            file=sys.stdout, flush=False):
    L = [str(obj) for obj in args] # ['1', '2', '3', '4']
    file.write(sep.join(L))
    file.write(end)  # 输入末尾字符
    if flush:
        file.flush()  # 清空缓冲区

myprint(1, 2, 3, 4, end='', flush=True)
while True:
    pass
