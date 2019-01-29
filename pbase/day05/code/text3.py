#  2.输入一个数，判断是不是素数
while True :   
    num = input("输入一个数:")
    if num != '#':
        num = int(num)
        if num == 2 or num == 3:
            print("这个数是素数")
        else:    
            for x in range(2,num):
                if num%x == 0:
                    print("不是素数")
                    break
            else:
                print("这个数是素数")
    else:
        break   

