# 练习:
#   写一个计算公式的解释执行器, 已知有如下一些函数 
#     def myadd(x, y):
#         return x + y
#     def mysub(x, y):
#         return x - y
#     def mymul(x, y):
#         return x * y
#     ...
#   另有一个函数get_func,有一个参数op 代表用给定的字符串
#     def get_func(op):
#         ...  # 此处要添加代码
#     此函数在传入字符串"加" 或 '+' 时返回myadd 函数
#     此函数在传入字符串"减" 或 '-' 时返回mysub 函数
#     ...
#   在主函数中:
#     def main():
#         while True:
#            s = input("请输入计算公式": )  # 10 加 20
#            L = s.split(' ')   # L = ['10', '加', '20']
#            a = int(L[0])
#            b = int(L[2])
#            fn = get_func(L[1])
#            print("结果是:", fn(a, b))  # 结果是: 30
#     main()



def myadd(x, y):
    return x + y
def mysub(x, y):
    return x - y
def mymul(x, y):
    return x * y
# ...

def get_func(op):
    if op == '加' or op == '+':
        return myadd
    elif op == '减' or op == '-':
        return mysub
    elif op in ('乘', '*'):
        return mymul

def main():
    while True:
        s = input("请输入计算公式: ")  # 10 加 20
        L = s.split(' ')   # L = ['10', '加', '20']
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print("结果是:", fn(a, b))  # 结果是: 30
main()

