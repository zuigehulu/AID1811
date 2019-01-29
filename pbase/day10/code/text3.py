def myfac(x):
    sum = 1
    for ch in range(1,x+1):
        sum *= ch 
    return sum
print(myfac(5))