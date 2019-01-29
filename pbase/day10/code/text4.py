def myhe(x):
    sum = 1
    for ch in range(2,x+1):
        sum += ch ** ch
    return sum
print(myhe(3))