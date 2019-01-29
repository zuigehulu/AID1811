l = [100,2,3,7,6,10,2,2,1]
x = 0
y = 0
while x < len(l):
    y = x
    while y < len(l):
        if l[x] > l[y] :
            l[x],l[y] = l[y],l[x]
        y += 1
    x += 1
print(l)