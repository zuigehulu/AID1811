#打印圣诞树
num = int(input("请输入树干的高度:"))

for i in range(1,num*2+1):
    if i <=num:
        print(" "*(num-i)+"*"*(i*2-1))
    else:
        print(" "*(num-1)+"*")