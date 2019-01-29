#打开一个文本文件，并向内部写入内容
def write_file():
    try:
        f = open('mynote.txt','a')
        f.write('hello')
        f.write('world')
        f.close()
        print('写入文件成功')
    except OSError:
        print('打开文件失败')
