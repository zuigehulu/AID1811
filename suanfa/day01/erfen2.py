L =[1,2,3,4,5,6,7,8,9,10,11,12,13]
key = 19
left = 0
right = len(L)-1
while left <= right:
    mad = (left + right)//2
    if L[mad] == key:
        print(mad)
        break
    elif L[mad] < key:
        left = mad + 1
    elif L[mad] > key:
        right = mad - 1
else:
    print("值不存在")
