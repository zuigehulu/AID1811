#   1. 试写一个递归函数 mysum(n), 此函数用递归方式求
#     1 + 2 + 3 + 4 + .... + n 的和
#     def mysum(n):
#         .... # 此处自己实现
#     print(mysum(100))  # 5050

# 1 + 2 + 3 + 4 + ..... + 98 + 99 + 100
# 100 + 99 + 98 + 97 + ..... + 3 + 2 + 1

#先假设 mysum已经实现原有的功能
def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n - 1)

print(mysum(100))  # 5050
