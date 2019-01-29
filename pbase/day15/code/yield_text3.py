def myfilter(func,iterable): 
    # return (x for x in range(iterable)if func(x))
    # for x in iterable:
    #     if func(x):
    #         yield x
    return (x for x in iterable if func(x))
def myfilter_laoshi(func,iterable):
    it = iter(iterable)
    while True:
        try:
            x = next(it)
            if func(x):
                yield x
        except StopIteration:
            return
for i in myfilter_laoshi(lambda x:x%2 ==1,range(10)):
    print(i)
for i in myfilter(lambda x:x%2 ==1,range(10)):
    print(i)

    