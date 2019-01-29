L = [1101,1102,1103,1104]
Y = ["小米音箱","MacPro","iPhone56","AppleWatch"]
# Ｌ中的编号分别对应Ｙ中的商品
# 编写程序：
# 当用户输入商品编号，将相对应的商品插入一个新的列表
# 当用户输入"p"打印已经添加的商品
# 当用户输入＂q＂退出程序并打印以添加商品
Z = []
while True:
    x=int(input("请输入商品编号:"))
    bianhao = x-1101
    Z += [x] +[Y[bianhao]]
    jieshou = input("继续(w):查看(p):结束(q)：")
    if jieshou == 'w':
        continue
    elif jieshou == "p":
        print(Z)
    elif jieshou == "q":
        print(Z)
        break
    

    