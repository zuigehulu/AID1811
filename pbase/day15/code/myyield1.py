def myyield():
    print("即将生成２")
    yield x
    print("生成器生成结果")

gen = myyield()  #调用生成器函数生成一个生成器
print(gen)      #generator
it = iter(gen)      #生成器中获取一个迭代器
print(next(it))
print(next(it))　　　#触发StopIteration异常

