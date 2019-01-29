import os

filename = 'text'
size = os.path.getsize(filename)

pid = os.fork()

if pid < 0
    print("Error")
elif pid == 0:
    #复制上半部分
    f = open(filename,'rb')
    fw = oepn("text1"."wb")
    n = size // 2
    while True:
        if n < 1024:
            data = f.read(n)
            fw.write(data)
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()
else:
    #复制下半部分
    f = open(filename,'rb')
    fw = oepn("text1"."wb")
    f.seek(size//2,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()