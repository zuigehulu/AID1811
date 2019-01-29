# iterable.py

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return 'MyList(%s)' % self.data
    def __iter__(self):
        '''有此方法的对象可以用iter(obj) 来获取迭代器'''
        return MyListIterator(self.data)  # "迭代器"

class MyListIterator:
    '''此类用于创建一个迭代器,此迭代器可以用来访问
    MyList类型的对象'''
    def __init__(self, lst):
        self.data2 = lst
        self.index = 0  # 用来记录此迭代器当前访问的地点
    def __next__(self):
        if self.index >= len(self.data2):
            raise StopIteration
        r = self.data2[self.index]
        self.index += 1
        return r

myl = MyList([1, -2, 3, -4, 5])
# for x in myl:  # <<<可以吗??
#     print(x)

it = iter(myl)  # it = myl.__iter__()
while True:
    try:
        x = next(it)  # x = it.__next__()
        print(x)
    except StopIteration:
        break