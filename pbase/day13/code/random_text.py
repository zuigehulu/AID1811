import random
rad = random.randint(0,100)
while True:
    s = int(input("请输入数字的大小"))
    if s == rad:
        print("猜对了")
        break
    elif s > rad:
        print("大了!")
    else:
        print("小了！")