try:
    myf = open("./pbase/day16/code/myfile.txt")
    print("打开文件成功")
    s = myf.readline()
    print("读取%d个字符"%len(s),"内容是:",s)
    myf.close()
except OSError:
    print("打开文件失败")