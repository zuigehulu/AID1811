# ３．分解质因数，输入一个正整数，分解质因数
# 输入９０
# 打印　９０　＝　２＊３＊３＊５
# 注：质因数是指最小能被原数整数的素数（不包括１）
zhenshu = int(input("输入一个正整数:"))

def zhishu(zhenshu):
    L = []
    for z in range(2,zhenshu):
        a = sushu(z)
        if a ==None:
            continue
        L.append(a)
    return L
def sushu(z):
    for x in range(2,z):
        if z%x == 0:
            break
    else:
        return z
    return None
L = zhishu(zhenshu)
S = []
def panduan(zhenshu,L,indx):
        if len(L) > indx:
            a = L[indx]
        else:    
            return 
        if zhenshu % a != 0:
            panduan(zhenshu,L,indx+1)
        elif zhenshu % a == 0:
            y =zhenshu/a
            S.append(a)
            panduan(y,L,indx)
panduan(zhenshu,L,0)
if S == []:
    S.append('1')
    S.append(zhenshu)
print(zhenshu,"=",end = " ")
str1 = ''
for x in S:
     str1 += str(x)+" x "

print(str1[:len(str1)-3])