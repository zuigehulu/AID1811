d = {}
while True:
    danci = input("请输入单词:")
    if danci =="":
        break
    else:
        jieshi = input("请输入解释:")
    d[danci] = jieshi
while True:
    cha = input("请输入要查的单词:")
    if cha == "":
        break
    if cha in d:
        print(cha,":",d[cha])
    else:
        print("没有此单词")