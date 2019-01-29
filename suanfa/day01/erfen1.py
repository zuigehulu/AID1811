def binary(value,key,left,right):
    middle = (left+right)//2
    if value[middle] == key:
        return middle
    elif value[middle] > key:
        return binary(value,key,left,middle-1)
    elif value[middle] < key:
        return binary(value,key,middle+1,right)

if __name__ =='__main__':
    L =[1,2,3,4,5,6,7,8,9,10,11,12,13]
    key = 9
    res = binary(L,key,0,len(L)-1)
    print(res)