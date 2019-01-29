def f4(a,b):
    print(id(a))
    a = a + b
    print(a)
    print(id(a))
a = 10
b = 20
f4(a,b)
print(a)
print(id(a))