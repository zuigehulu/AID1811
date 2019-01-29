import sys
def myprint(*args,sep=' ',end = '\n',
            file = sys.stdout,flush = False):
    flag = False
    for obj in args:
        s = str(obj)
        if flag:
            file.write(sep)
        flag = True
        file.write(s)      
    file.write(end)

myprint(1,2,3,4)
myprint(3,4,5,6,sep = '#',end = '\n***\n')
