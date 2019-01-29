l =[1,2,3,4,5,34,4,4,5,2,1,7,1]
yi = []
duo = []
for x in l:
    num =l.count(x)
    if num == 1:
        yi += [x]
    elif num > 1:
        if x not in duo:
            duo += [x]
print(yi)
print(duo)