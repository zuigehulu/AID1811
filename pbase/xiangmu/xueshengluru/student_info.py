# student_info
from student_class import *
from student_menu import *
from student_shuchu import *

#进行判断排序，根据选择进行排序
def panduan_paixu(jieshoupaixu,L):
    if jieshoupaixu == "1":
            pai_xu('1',True,L)
            # paixu('scire',True,L)         
    elif jieshoupaixu == "2":
        pai_xu('2',False,L)         
    elif jieshoupaixu == "3":
        pai_xu('3',True,L)          
    elif jieshoupaixu == "4":
        pai_xu('4',False,L)         
    else:
        return

#将列表按成绩从大到小排序
def pai_xu(bianliang,revs,L):
    if bianliang == '1' or bianliang == '2': 
        L1 = sorted(L,key = lambda x : x.score,reverse = revs)
        output_student(L1)
    if bianliang == '3' or bianliang == '4':
        L1 = sorted(L,key = lambda x : x.age,reverse = revs)
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
                    # d={"name":name,"age":age,"scire":scire}
                    # fangru_wenjian(d)   #将字典放入文件中
                    s = Student(name,age,scire)
                    # s.shuru_wenjian()
                    L.append(s)
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
# def fangru_wenjian(d):
#     try:
#         fw = open('./pbase/xiangmu/xueshengluru/s1.txt','at')
#         d = str(d)
#         fw.write(d)
#         fw.write('\n')
#     except OSError:
#         print("加入失败")
#     finally:
#         fw.close()
#删除学生信息
def shanchu(xinxi,L): 
    qingping()  
    # for x in L:
    #     for ch in x.values():
    #          if xinxi == ch:
    #             print('名字',x.name,'年龄',x.age,'成绩',x['scire'])
    #             shifou = input("是否删除(Ｙ／Ｎ)")
    #             if shifou == 'y':
    #                 L.remove(x)
    #                 return           
    # else:
    #     print("抱歉,没有这个学生信息")
    for x in L:
        if x.name == xinxi:
            L.remove(x)
            print("删除成功")
            fanhui()
            return
    else:
        print("抱歉，没有这个学生信息")


#查找学生信息
def chazhao(xinxi,L):   #查找学生信息
    for x in L:
        # for ch in x.values():
        #     if xinxi == ch:
        #         print('名字',x['name'],'年龄',x.age,'成绩',x['scire'])
        #         fanhui()
        #         return
        if x.name == xinxi:
            x.shuchu_xuesheng_xinxi()   
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
    fr = open("./s1.txt",'wt')
    for ch in L1:
        fr.write(ch.name)
        fr.write(',')
        fr.write(str(ch.age))
        fr.write(',')
        fr.write(str(ch.score))
        fr.write(',')
        fr.write('\n')
        xianshi.append("+"+"-"*(60)+"+")
        if ord(ch.name[0]) >255:
            xianshi.append(("|"+ch.name.center(22-len(ch.name))+"|"+str(ch.age).center(18)+'|'+
            str(ch.score).center(18)+"|"))
        else:
            xianshi.append(("|"+ch.name.center(22)+"|"+str(ch.age).center(18)+'|'+
            str(ch.score).center(18)+"|")) 
    fr.close()   
    xianshi.append(("+"+"-"*(60)+"+"))
    xianshihanshu(xianshi)

#从文件中读取数据，并放入list中
def read_txt(Ｌ):
    try:
        L = Student.L
        return L
    except OSError:
        print("导入失败")
    finally:
        fr.close()
    
    # try:
    #     # fr = open("./pbase/xiangmu/xueshengluru/s1.txt",'rt')
    #     while True:
    #         d = fr.read()
    #         if d == '':
    #             break
    #         s ='''global d2;d2='''+d.strip()           
    #         exec(s)            
    #         L.append(d2)
    #         # print(L)
    # except OSError:
    #     L = []
    #     print("打开失败")
    # finally:
    #     # fr.close()
    # return L
# L =[]
# read_txt(L)

# 每次操作的返回函数
def fanhui():
    while True:
        e = input("是否返回(N/Y)")
        if e == 'y':
            return 
