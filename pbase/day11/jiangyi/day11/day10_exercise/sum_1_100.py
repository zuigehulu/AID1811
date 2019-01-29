#   2. 写一个函数 mysum(x) 来计算:
#      1 + 2 + 3 + 4 + .... + x 的和,并返回
#      (要求: 不允许调用sum函数)
#      如:

# 方法1
# def mysum(x):
#     s = 0
#     for i in range(1, x + 1):
#         s += i
#     return s

# 方法2
def mysum(x):
    s = sum(range(1, x + 1))
    return s

print("1+2+3+...+100的和是", mysum(100))  # 5050

# 方法3
print(sum(range(1, 101)))  # 函数式编程