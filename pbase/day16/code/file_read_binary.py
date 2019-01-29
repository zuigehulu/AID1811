try:
    fr = open("myfile.txt",'rb')
    b = fr.read(13)
    print(b)
    s = b.decode()
    print(s)
    fr.close()
except OSError:
    print("出错")