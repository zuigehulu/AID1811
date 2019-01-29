# file_read.py

# 此示例示意读取文件myfile.txt里的内容

try:
    # myf = open("/home/tarena/aid1811/pbase/day16/code/myfile.txt")
    myf = open("myfile.txt")
    print("打开文件成功")
    # 读取文件内容
    while True:
        s = myf.readline()  # 每次读一行
        if not s:
            print("读文件结束")
            break
        print("读取%d个字符" % len(s), '内容是:', s)

    myf.close()
except OSError:
    print("打开文件失败")