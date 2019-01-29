def myyield():
    yield 2
    yield 4
    yield 5
    yield 6
    yield 7

    print("生成器生成结果")

gen = myyield()  #调用生成器函数生成一个生成器
for x in gen:
    print(x)

