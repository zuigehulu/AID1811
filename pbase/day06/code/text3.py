# 已知有一个列表重存在很多重复的数
# Ｌ = [1,3,2,1,6,4,2,....,98,82]
# 将列表中出现的数字存入一个列表Ｌ２重
# 要求:去重
# 将Ｌ列表重出现２次的数字存入另一个Ｌ３
L = [1,3,2,1,5,6,7,8,64,3,2,1,2,4,5,6]
L1 =[]
liangci  = [] 
for x in L:
    if x not in L1:
        L1 += [x]
    sum = 0
    for y in L:
        if x == y:
            sum += 1
    if sum == 2:
        if x not in liangci:
            liangci += [x]
print(L1)
print(liangci) 