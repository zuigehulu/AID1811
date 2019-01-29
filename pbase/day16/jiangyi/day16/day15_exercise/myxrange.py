#   1. 实现一个python2下的xrange([start], stop, [step])
#     生成器函数,此生成函数按range规则来生成一系列整数
#     要求:
#       myxrange功能与range功能完全相同
#       不允许调用range函数和列表
#   用自己写的myxrange结果生成器表达式求 1~10以内所有奇数的
#     平方和
#   如:
#     def myxrange(start, stop=None, step=None):
#          ....以下自己实现
#     求:1 ** 2 + 3 ** 2 + 5 **2 + ...  9 ** 2



def myxrange(start, stop=None, step=None):
    if stop is None: # 没有第二个参数:
        stop = start
        start = 0
    if step is None:
        step = 1

    if step > 0:  # 正向生成
        while start < stop:
            yield start
            start += step
    elif step < 0:  # 反向生成
        while start > stop:
            yield start
            start += step  # 因为 step为负数


print(sum(
          (x**2 for x in myxrange(1, 10, 2))
         )
     )
