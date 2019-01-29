# 扑克牌，只取红桃花色13，用数字1-13表示。洗牌后，将牌反面朝上排成一排，找到红桃6。
#   问题：怎么找，使用Python实现该过程。
import random
L = [1,2,3,4,5,6,7,8,9,10,11,12,13]
random.shuffle(L)
j = 1
for i in L:
    if i == 6:
        print(L)
        print(j)
        break
    j += 1
else:
    print("没有该数字")