class MyList:
    def __init__(self,interable):
        self.data = [x for x in interable]
    def __repr__(self):
        return "MyList(%s)"%self.data
    def __iter__(self):
        return MyListIterator(self.data)

class MyListIterator:
    '''此类用来创建一个迭代器，
    此迭代器可以用来访问MyList类型的对象
    '''
    def __init__(self,lst):
        self.data = lst
        self.index = 0   #用来记录此迭代器当前访问的地点
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        r = self.data[self.index]
        self.index += 1       
        return r

myl = MyList([1,2,3,4,5])
it =iter(myl)
while True:
    try:
        s =next(it)
        print(s)
    except StopIteration:
        break
