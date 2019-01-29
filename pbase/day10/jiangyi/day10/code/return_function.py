# return_function.py

# 此示例示意函数可以返回另一个函数的引用关系
def get_function():
    s = input("请输和您要做的操作: ")
    if s == '求最大':
        return max
    elif s == '求最小':
        return min
    elif s == '求和':
        return sum

L = [2, 4, 6, 8, 10]
f = get_function()
print(f(L))







