import sys
def myprint(*args,sep=' ',end = '\n',
            file = sys.stdout,flush = False):
    flag = False
    L = [str(obj) for obj in args]
    file.write(sep.join(L))    
    file.write(end)

myprint(1,2,3,4)
myprint(3,4,5,6,sep = '#',end = '\n***\n')
