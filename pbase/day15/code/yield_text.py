def myeven(start,stop):
    for x in range(start,stop):
        if x % 2 == 0:
            yield x
            

evens = list(myeven(10,20))
print(evens)
for x in myeven(21,30):
    print(x)