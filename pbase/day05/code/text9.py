l = [1,2,3,4,5,34,4,4,5,2,1,7,1]
yi = []
duo = []
for x in l:
    sum = 0
    jishu = 0
    for y in l:
        if x == y:
            if jishu == 0:
                sum += 1
                l = l[jishu+1:]               
                jishu -= 1
            elif jishu == len(l):
                sum += 1
                l = l[:jishu]
                jishu -= 1
            else:
                sum += 1
                l = l[:jishu] + l[jishu+1:]
                jishu -= 1
        jishu += 1
    if sum == 1:
        yi += [x]
    elif sum > 1:
        duo += [x]
print(yi)
print(duo)
