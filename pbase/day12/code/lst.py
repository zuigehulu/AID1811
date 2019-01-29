L = [1,2,3]
def f(n = 0,lst = []):
    lst.append(n)
    print(lst)
    # lst.clear()
f(4,L)
f(5,L)
f(100)
f(200)

#-----------------------------
#进行改进，可重入
L = [1,2,3]
def f1(n = 0,lst = None):
    if lst is None:
        lst = []
    lst.append(n)
    print(lst)

f1(4,L)
f1(5,L)
f1(100)
f1(200)