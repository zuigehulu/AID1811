# 练习:
#   写一个函数 myadd, 此函数可以计算两个数,三个数和四个数的和
#   如:
#     def myadd(....):
#         ...
    
#     print(myadd(10, 20))         # 30
#     print(myadd(100, 200, 300))  # 600
#     print(myadd(1, 2, 3, 4))     # 10

def myadd(a, b, c=0, d=0):
    s = a + b + c + d
    return s

print(myadd(10, 20))         # 30
print(myadd(100, 200, 300))  # 600
print(myadd(1, 2, 3, 4))     # 10
