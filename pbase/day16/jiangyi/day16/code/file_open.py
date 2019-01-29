# file_open.py

# 此示例示意 文件的打开和读文件操作

try:
    # 打开文件
    # myfile = open("./myfile.txt")  # 正常打开成功
    myfile = open("./myaaaa.py")  # 打开失败

    print("打开文件成功")
    # 读/写文件

    # 关闭文件
    myfile.close()
    print("关闭文件成功")
except OSError:
    print("文件打开失败")