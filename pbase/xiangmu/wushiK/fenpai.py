import copy
import random 

#根据人数建立牌组
def pai_zu():
    huase = ('红桃','梅花','方片','黑桃')
    paizu1 = []
    for y in huase:      
        for x in range(1,14):
            paizu1.append({y:x})
    paizu1.append({'红':'大王'})
    paizu1.append({'黑':'小王'})
    return paizu1

#分牌操作
def fen_pai(x,paizu):
    if x == 4:
        paizu2 =copy.deepcopy(paizu)
        # print(paizu,paizu2)
        return fenpai_2(paizu,paizu2)   #将两副牌分给四个人
    elif x == 6:
        paizu2 =copy.deepcopy(paizu)
        paizu3 =copy.deepcopy(paizu)
        return fenpai_3(paizu,paizu2,paizu3)
        #将三副牌分给六个人

#将两副牌分给４个人
def fenpai_2(paizu1,paizu2):
    dict1={}
    lst = []
    for x in range(1,4):
        lst=random.sample(paizu1,13)
        lst.extend(random.sample(paizu2,13))
        print(lst)
        dict1[x] = lst
    return dict1
ren_shu = int(input("参加的人数有(4/6):"))
paizu = pai_zu()
# print(paizu)
fen_pai_2=fen_pai(ren_shu,paizu)
# print(fen_pai_2)

