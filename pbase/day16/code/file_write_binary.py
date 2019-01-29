b = bytes(range(256))
try:
    fw = open("mybinary.txt",'wb')
    fw.write(b)
    fw.close
except OSError:
    print("写文件失败")