# 1.有一只小猴子，摘了很多桃
# 第一天吃了全部桃子的一半，感觉不饱又吃了一个
# 第二天吃了剩下的一半，感觉不饱又吃了一个
# 以此类推，第１０天发现剩下一个了，请问一天摘了多少桃子
x = 1
for y in range(1,10):
    z = (x+1)*2
    x = z
print(z)