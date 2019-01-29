#	用fork创建父子进程，同时复制一个文件，各复制一半到一个新的文件中
import os
daxiao = os.path.getsize('day4.txt')
print(daxiao)
pid = os.fork()
if pid < 0:
    print("Error")
elif pid == 0:
    fr = open("day4.txt",'rb')
    fw = open('day04_1.txt','wb')
    chang = daxiao//2   
    data = b''          
    while True:
        chang -= len(data)
        if chang >= 1024:
            data = fr.read(1024)
            fw.write(data)         
        elif chang < 1024:
            data = fr.read(chang)
            fw.write(data)
            break
    fw.close()
    fr.close()
    print("子程序结束")
    daxiao1 = os.path.getsize('day04_1.txt')
    print(daxiao1)
else:
    fr = open("day4.txt",'rb')
    fw = open("day04_2.txt",'wb')
    fr.seek(daxiao//2,0)
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fw.close()
    fr.close()
    print('程序结束')
    daxiao1 = os.path.getsize('day04_2.txt')
    print(daxiao1)
