#写一个计算公式的解释执行器
def myadd(x,y):
    return x + y
def mysub(x,y):
    return x - y
def mymul(x,y):
    return x * y
def chu(x,y):
    return x / y
def quyu(x,y):
    return x % y

#另有一个函数get_func　有一个参数op　
# 代表给大的字符串

def get_func(op):
    if op == '+'　or op == '加':
        return myadd
    elif op == '*' or op == '乘':
        return mymul
    elif op == '-' or op == '减':
        return mysub
    elif op == '/' or op == '除':
        return chu
    elif op == '%' or op == '余':
        return quyu
def main():
    while True:
        s = input("请输入计算公式(10 + 20):")
        if s == "":
            break
        L = s.split(' ')
        a = int(L[0])
        b = int(L[2])
        fn = get_func(L[1])
        print("结果是:",fn(a,b))
# 调用main函数
main()
