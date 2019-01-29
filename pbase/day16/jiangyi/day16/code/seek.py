# seek.py

# 此示例示意用文件流对象的seek方法来移动文件的读写指针位置
try:
    fr = open("byte20.txt", 'rb')
    b = fr.read(2)
    print(b)  # 'AB'
    print("当前的读写位置是:", fr.tell())  # 2
    # 以下读取第5~10个字节 b'abcde'
    # fr.seek(5, 0)  # 从文件头向后移动5个字节
    # fr.seek(3, 1)  # 从当前位置向后移动3个字节
    fr.seek(-15, 2)  # 从文件尾向前移动15个字节
    print("移动后的读写位置是: ", fr.tell())  # 5
    b = fr.read(5)  #  b'abcde'
    print("移动后: b=", b)

    fr.close()
except OSError:
    print("打开文件失败!!")
