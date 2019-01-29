i = 1
j=0
while i <= 100:
    if i % 3 ==0 or i % 7 ==0:
        if i % 3 == 0 and i % 7 == 0:
            pass
        else:
            print(i,end = " ")
            j = j+1
    i += 1
else:
    print()
print(j)