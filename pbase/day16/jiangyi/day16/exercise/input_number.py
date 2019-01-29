#   1. 写一个程序,让用户输入很多个正整数,
#     最后将这些整数存于文件 mynumbers.txt中
#     如:
#       请输入: 1
#       请输入: 2
#       请输入: 3
#       请输入: 4
#       请输入: -1  # 结束
#     格式自己定义

try:
    fw = open("mynumbers.txt", 'w')
    try:
        # 读取数据并写入文件中:
        while True:
            n = int(input("请输入正整数: "))
            if n < 0:
                break
            fw.write(str(n))  # 先转为字符串再写
            fw.write('\r')
            fw.write('\n')
    finally:
        fw.close()
except OSError:
    print("打开失败!")
except ValueError:
    print("输入内容错误!!!")
