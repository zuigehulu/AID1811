def fry_egg():
    print("打开天然气点燃火")
    try:
        try:
            count = int(input("请输入鸡蛋个数:"))
            print("完成煎鸡蛋，共煎了%d的鸡蛋",count)
        finally:
            print("关闭天然气")
    except ValueError:
        print("煎鸡蛋失败")

fry_egg()