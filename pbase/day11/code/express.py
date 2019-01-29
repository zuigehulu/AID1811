def press(x):
    if x == 1:
        return 1
    return x**x + press(x-1)
print(press(3))

def fun(x):
    return sum(map(lambda x:x**x,range(1,4)))
print(fun(3))