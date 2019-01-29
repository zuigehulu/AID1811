l = [20,1,2,3,7,6,10,2,2]
i = 0
j = 0
for x in l:
    for y in l:
        if x > y :
            i = l.index(x)
            j = l.index(y)
            l[i] = y
            l[j] = x
        
print(l)