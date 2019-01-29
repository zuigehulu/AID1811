L = [3,5]
print(id(L))
L[0:0] = [1,2]
L[3:3] = [4]
L[5:5] = [6]
print(L)
L[:]= L[-1:-len(L):-1]
# L = L[5:0:-1] 
print(L)
print(id(L))