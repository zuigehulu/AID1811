# def3.py

# 此示例示意定义带有形参的函数,
# 此函数叫mymax,此函数能接收两个实际调用参数,在函数内部
# 找出最大的一个打印在终端上

def mymax(a, b):
    if a > b:
        print("最大值是:", a)
    else:
        print("最大值是:", b)

# 调用有参数的函数
mymax(100, 200)  # 最大值是: 200
mymax("ABC", 'abc')  # 最大值: abc

