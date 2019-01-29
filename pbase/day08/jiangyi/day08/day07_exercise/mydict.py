
#   2. 写一个程序,实现一个带有菜单界面的字典程序
#      菜单如下:
#         1) 添加单词
#         2) 删除单词
#         3) 查找单词
#         q) 退出
#     示例见:
#       mydict.py


d = {}  # 先有个容器
while True:
    print("1) 添加单词")
    print("2) 删除单词")
    print("3) 查找单词")
    print("q) 退出")
    s = input("请选择: ")
    if s == '1':
        # 做添加单词的操作
        key = input("请输入单词: ")
        value = input("请输入解释: ")
        if key in d:
            print("单词已经存在,添加失败!")
        else:
            d[key] = value
            print("添加成功")
    elif s == '2':
        key = input("请输入要删除的单词: ")
        if key in d:
            print("删除成功")
            del d[key]
        else:
            print("删除失败!")
    elif s == '3':
        key = input("请输入要查的单词: ")
        if key in d:
            print("解释是: ", d[key])
        else:
            print("查无此词!!!")
    elif s == 'q':
        break
