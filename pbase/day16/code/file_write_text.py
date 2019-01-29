def write_file():
    try:
        fw = open('mynumbers.txt','w')
        while True:
            s = int(input("请输入正整数"))
            if s < 0:
                break
            fw.write(str(s))
            fw.write('\n')
    except OSError:
        print('写入失败')
    finally:
        fw.close()
write_file()



