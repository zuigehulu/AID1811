# file_read_binary.py

try:
    fr = open('myfile.txt', 'rb')

    b = fr.read(10)
    # b = fr.read(12)  # 出错
    print(b)
    fr.close()
    s = b.decode()  # 出错
    print("解码之后的内容是:", s)

except OSError:
    print('文件打开失败!')
