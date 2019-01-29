list1 = [1001,1003,1008,1004]
list2 = ['tom','jerry','spike','tyke']
d = {list2[x]:list1[x] for x in range(4)}
print(d)

for x in range(4):
    d[list2(x)] = list1(x)