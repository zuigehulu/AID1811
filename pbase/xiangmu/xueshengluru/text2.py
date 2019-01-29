# student_info
from student_menu import *
from student_shuchu import *
def panduan_paixu(jieshoupaixu,L):
    if jieshoupaixu == "1":
            pai_xu('scire',True,L)
            # paixu('scire',True,L)         
    elif jieshoupaixu == "2":
        pai_xu('scire',False,L)         
    elif jieshoupaixu == "3":
        pai_xu('age',True,L)          
    elif jieshoupaixu == "4":
        pai_xu('age',False,L)         
    else:
        return
#将列表按成绩从大到小排序
def pai_xu(bianliang,revs,L):
    L1 = sorted(L,key = lambda x : x[bianliang],reverse = revs)
    output_student(L1)

#　输入学生的信息，包括姓名，年龄，成绩
def input_student(L):
    qingping()
    while True:
        while True:
            name = input("输入名字:")
            try:
                age = int(input("输入年龄:"))
                scire = int(input("输入成绩:"))
                if  0 <age <= 100 and 0 <= scire <= 100:
                    fangru_wenjian('"name":name,')
                    fangru_wenjian('"age":age,))
                    fangru_wenjian(str("scire":scire,))
                    # fangru_wenjian(d)   #将字典放入文件中
                    L.append(d)
                    break
                else:
                    raise ValueError
            except ValueError:
                print("输入错误，请重新输入")
                input()           
        panduan = input("是否继续（w:继续，q：退出）")
        if panduan == 'q':
            break
# 将字典格式的数据存入文件中
def fangru_wenjian(d):
    try:
        fw = open('./pbase/xiangmu/xueshengluru/s1.txt','at')
        # d = str(d)
        fw.write(d)
        # fw.write('\n')
    except OSError:
        print("加入失败")
    finally:
        fw.close()
#删除学生信息
def shanchu(xinxi,L): 
    qingping()  
    for x in L:
        for ch in x.values():
             if xinxi == ch:
                print('名字',x['name'],'年龄',x['age'],'成绩',x['scire'])
                shifou = input("是否删除(Ｙ／Ｎ)")
                if shifou == 'y':
                    L.remove(x)
                    return           
    else:
        print("抱歉,没有这个学生信息")

#查找学生信息
def chazhao(xinxi,L):   #查找学生信息
    for x in L:
        for ch in x.values():
            if xinxi == ch:
                print('名字',x['name'],'年龄',x['age'],'成绩',x['scire'])
                fanhui()
                return
    else:
         print("没有此学生信息")
    fanhui()

# 显示录入的学生信息
def output_student(L1):
    xianshi = []
    xianshi.append(("+"+"-"*(60)+"+"))
    xianshi.append("|"+"学生信息管理系统".center(52)+"|")
    xianshi.append(("+"+"-"*(60)+"+"))
    xianshi.append(('|'+'姓名'.center(20)+"|"+
            "年龄".center(16)+"|"+
            "成绩".center(16)+"|"))
    for ch in L1:
        xianshi.append("+"+"-"*(60)+"+")
        if ord(ch['name'][0]) >255:
            xianshi.append(("|"+ch['name'].center(22-len(ch['name']))+"|"+str(ch['age']).center(18)+'|'+
            str(ch['scire']).center(18)+"|"))
        else:
            xianshi.append(("|"+ch['name'].center(22)+"|"+str(ch['age']).center(18)+'|'+
            str(ch['scire']).center(18)+"|"))     
    xianshi.append(("+"+"-"*(60)+"+"))
    xianshihanshu(xianshi)

#从文件中读取数据，并放入list中
def read_txt(Ｌ):
    try:
        fr = open("./pbase/xiangmu/xueshengluru/s1.txt",'rt')
        while True:
            d = fr.read()
            if d == '':
                break
            s = 'd1 = {} \n d1='+d.strip()
            # s2 = s+'\n L.append(d)'
            # d1 = dict(l1[0])
            exec(s)
            L.append(d1)
    except OSError:
        L = []
        print("打开失败")
    finally:
        fr.close()
    return L
L =[]
read_txt(L)