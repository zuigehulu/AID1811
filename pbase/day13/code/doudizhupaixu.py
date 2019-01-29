# 写一个程序，模拟斗地主发牌，牌共５４张，
#黑桃　\u2660  梅花 \u2663  红桃\u2665 方块\u2666

#生成一副扑克牌，有54张，４个花色，大小王．
# 花色用来判定同样数值时产生先后顺序，牌值表示牌，大小表示牌的大小
def shengcheng_puke():
    L = []
    puke_yizu = {
        1: 'A',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10:'10',
        11:'J',
        12:'Q',
        13:'K'
    }
    for x in ('\u2660','\u2663','\u2666','\u2665'):
        for y in range(1,14):
            L.append({'花色':x,'牌值':(x+puke_yizu[y]),'大小':int(y)})
    L.append({'牌值':'大王','大小':201,'花色':'\u2550'})
    L.append({'牌值':'小王','大小':200,'花色':'\u2550'})

    return L
#把一副牌分成４份，三个人和底牌组成列表
def fenpai(L):
    import random
    import copy
    L1 = copy.deepcopy(L)
    random.shuffle(L1)
    sanrenpai = [L1[:3]]
    for x in range(3):
        y = 0
        yirenpai = []
        for z in range(17):
            s = L1.pop()
            yirenpai.append(s)
            y += 1
        sanrenpai.append(yirenpai)
    return sanrenpai
#将牌从大到小，方块／红桃／梅花／黑桃进行排列
def daxiao(L):
    for x in range(len(L)):
        for y in range(len(L)):
            if L[x]['大小'] > L[y]["大小"]:
                L[x],L[y] = L[y],L[x]  
            elif L[x]['大小'] == L[y]['大小']:
                if L[x]['花色'] > L[y]['花色']:
                    L[x],L[y] = L[y],L[x]
    # print(L)
    return L                  

#将三个人的牌和底牌依次排序输出 
def paixu_shuchu(L):
    L1 = daxiao(L) 
    for x in L1:
        print(x['牌值'],end =' ')
    print()       
        
#把每个人的牌输出：
def shuchu(L):
    print("第一个人的牌:")
    paixu_shuchu(L[1])
    s = input()
    print("第二个人的牌:")
    paixu_shuchu(L[2])
    s = input()
    print("第三个人的牌:")
    paixu_shuchu(L[3])
    s = input()
    print("底牌:")
    paixu_shuchu(L[0])
#主函数
def main():
    pukepai = shengcheng_puke()
    fenhaopai = fenpai(pukepai)
    # print(fenhaopai)
    shuchu(fenhaopai)

main()