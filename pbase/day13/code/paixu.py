L=[3,4,2,1,4,6]
for x in range(len(L)):
    for y in range(len(L)):
        if L[x] < L[y]:
           L[x],L[y] = L[y],L[x] 
       

print(L)