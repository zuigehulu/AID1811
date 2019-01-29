try:
    fb = open('myprint.txt','rb')
    b = fb.read(2)
    print(b)
    print("当前的读写位置是：",fb.tell())
    # fb.seek(5,0) #从文件头向后移动５个字节
    #fb.seek(3,1) #从当前位置向后移动３个字节
    fb.seek(20,0) #从末尾向前移动１５个字节
    b = fb.read(10)
    print(b)
    print("当前的读写位置是：",fb.tell())
    fb.close()
except OSError:
    print("错误")