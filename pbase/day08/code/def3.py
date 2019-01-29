#此示例示意定义带有行参的函数
#此函数能接收两个实际调用参数，在函数内部

def mymax(a,b):
    # if a > b:
    #     print("a最大")
    # else:
    #     print("b最大")
    return max(a,b)
#调用有参数的函数
print(mymax(100,200))
print(mymax("ABC","ABCD"))