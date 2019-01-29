# file_write_binary.py

# 此示例示意向一个文件中写入256个字节
# 字节值从0~255

b = bytes(range(256))

try:
    fw = open("mybinary.txt", 'wb')
    fw.write(b)  #  写入字节串
    fw.close()
except OSError:
    print("写文件失败!!!")

