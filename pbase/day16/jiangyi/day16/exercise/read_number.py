# read_number.py

# 此示例示意将mynumber.txt里的内读取出来.打印和

try:
    fr = open("mynumbers.txt", 'r')
    L = []
    while True:
        s = fr.readline()
        if not s:
            break
        L.append(int(s.rstrip()))
    fr.close()
except OSError:
    print('打开文件失败 ')

print("和是:", sum(L))
