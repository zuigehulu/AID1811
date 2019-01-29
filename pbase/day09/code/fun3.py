a = [1,2,3]
b = 200
def f3(x,y):
    x = x+[y] 
f3(a,b)
print(a)
print(b)
def f4(a,b):
    print(id(a))
    a = a+[b]
    print(a)
    print(id(a))
f4(a,b)
print(a)
print(id(a))