def myinteger(n):
    i = 0
    while i < n:
        yield i 
        i += 1

for x in myinteger(10):
    print(x)

it = iter(myinteger(20))
print(next(it))
print(next(it))

L = [x for x in myinteger(20) if x%2 ==1]
print(L)