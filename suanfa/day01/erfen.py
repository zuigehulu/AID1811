# 扑克牌，取红方色牌13张，使用1-13来表示
# 13张牌从小到大排序后，将牌反面朝上，找出红方9

def erfen(values,num):
    s = len(values)//2
    if values[s-1] < num:
        data = erfen(values[s-1:],num)
        return data + s -1
    elif values[s-1] > num:
        data = erfen(values[0:s-1],num)    
        return s-1-data
    elif values[s-1] == num:
        return s

if __name__ =="__main__":
    L = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    num = 9
    d = erfen(L,num)
    print(d)