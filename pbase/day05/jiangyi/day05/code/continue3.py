# continue.py

# 此示例示意continue语句的用法
# 用continue 语句来忽略奇数,打印偶数
# 用while语句来实现

num = 0
while num < 10:
    if num % 2 == 1:
        num += 1
        continue
    print(num)
    num += 1


# for num in range(10):
#     if num % 2 == 1:
#         continue
#     print(num)

