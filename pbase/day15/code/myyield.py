def myyield():
    for x in range(20):
        yield x
    print("即将生成２")
    print("生成器生成结果")

gen = myyield()
it = iter(gen)
print(next(it))
print(next(gen))

