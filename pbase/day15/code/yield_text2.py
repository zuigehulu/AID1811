L = [2,3,5,7]

def dongtai(L):
    return (x**2+1 for x in L)

def dongtai_1(L):
    for x in L:
        yield x**2+1
def lst(L):
    return [x**2+1 for x in L]
gen = iter(dongtai(L))
for x in gen:
    print(x,end = " ")
print()
gen1 = iter(dongtai_1(L))

for x in gen1:
    print(x,end = " ")
print()

for x in lst(L):
    print(x,end=' ')
print()