L = [(1,5),(3,9),(4,1),(3,6),(5,3)]

def paixu(x):
    return x[1]
L2 = sorted(L,key = paixu)
print(L2)

L3 = sorted(L,key = paixu , reverse = True)
print(L3)

def paixu2(x):
    return (x[1]**2 +x[0]**2)**0.5
      
L4 = sorted(L,key = paixu2)
print(L4)