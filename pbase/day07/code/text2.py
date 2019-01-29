# 写一个程序，
# 菜单：
# １．添加单词
# ２．删除单词
# ３．查找单词
# ４．q退出
def tianjia(danci1):    #添加单词
    danci1 = input("请输入单词:")
    if danci1 =="":
        return
    else:
        jieshi = input("请输入解释:")
        return jieshi

def shanchu():   # 删除单词
    if shan in d:
        return shan
    else:
        print("抱歉，没有这个单词")
def chazhao():   #查找单词
    if cha in d:
        print(cha,":",d[cha])
    else:
         print("没有此单词")
d = {}
while True:
    print("1.添加单词")
    print("2.删除单词")
    print("3.查找单词")
    print("4.(q)退出")
    num = input("请进行操作:")
    if num == '1':   #添加操作
        danci =
        jieshi_1 = tianjia(danci)
        if jieshi_1 != None:
            d[danci] = jieshi_1
        else:
            continue
    elif num == '2': #删除操作
        shan = input("请输入要删除的单词:")
        shan_danci = shanchu()
        if shan_danci != 0:
            d.pop(shan_danci)
    elif num == '3':        #查找操作
        cha = input("请输入要查的单词:")
        chazhao()
    elif num == 'q' :
        break

        
        
