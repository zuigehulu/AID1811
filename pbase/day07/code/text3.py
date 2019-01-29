# 如:请输入姓名:tarena
# 　请输入年龄：１５
# 　请输入成绩:98
# 形成存储格式:
# infos =[{'name':'tarena','age':15,'score':99}
# 　　　　　{'name':'xiaozhang','age':15,'score':99｝]

# 第二步，打印表格 
# +-------------------------------------+
# | 姓名   |      年龄 　 　｜　　成绩　　　｜
# +-------------------------------------+
# | tarena|    15         |    99       |
# +-------------------------------------+　　
L = []
while True:
    name = input("输入名字:")
    age = input("输入年龄:")
    scire = input("输入成绩:")
    d={"name":name,"age":age,"scire":scire}
    L.append(d)
    # print(L)
    panduan = input("是否继续（w:继续，q：退出）")
    if panduan == 'w':
        continue
    elif panduan == 'q':
        break
print("打印表格")
print("+"+"-"*(60)+"+")
print('|'+'姓名'.center(20)+"|"+
          "年龄".center(16)+"|"+
          "成绩".center(16)+"|")
for ch in L:
    print("+"+"-"*(60)+"+")
    if ord(ch['name'][0]) >255:
        print("|"+ch['name'].center(22-len(ch['name'])),end = "")
    else:
        print("|"+ch['name'].center(22),end = "")     

    print("|"+ch['age'].center(18)+'|'+
          ch['scire'].center(18)+"|")
print("+"+"-"*(60)+"+")