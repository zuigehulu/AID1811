def charu(value):
    for i in range(1,len(value)):
        temp = value[i]
        pos = i
        for j in range(i-1,-1,-1):
            if value[j] > temp:
                value[j+1] = value[j]
                pos = j
            else:
                pos = j + 1
                break
        value[pos] = temp

value = [80,70,30,50,69,78,90,100,65,88]
charu(value)
print(value)