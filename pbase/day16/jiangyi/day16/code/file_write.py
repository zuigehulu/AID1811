# file_write.py


# 此示例示意打开一个文本文件,并向里面写入内容

try:
    fw = open("mynote.txt", 'w')  # 创建文件并写,清空文件内容
    # fw = open("mynote.txt", 'x')  # 如果原文件存在则报错
    # fw = open("mynote.txt", 'a')  # 追加
    # 写字符串到方件中...
    fw.write("ABC\n")
    fw.write("hello")  # 写入5个字符
    fw.write("world\n")  # 写入5个字符
    fw.writelines( ["ABC", '123', '中文'] )
    fw.close()
    print("写入文件成功")
except OSError:
    print('打开文件失败')