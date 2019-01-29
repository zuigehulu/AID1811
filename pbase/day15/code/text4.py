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
i = 0
S = []
while True:
    if i == len(L):
        break
    if zhenshu% L[i] == 0:
        shu = L[i]
        S.append(shu)
        zhenshu /= L[i]
    else:
        i += 1
print(S)
    
