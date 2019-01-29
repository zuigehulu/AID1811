# len_overwrite.py

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __len__(self):
        '''此方法必须返回整数'''
        return self.data.__len__()
        # return len(self.data)

myl = MyList([1, -2, 3, -4, 5])
print(myl)  # MyList([1, -2, 3, -4, 5])
print(len(myl))  # print(myl.__len__())

myl2 = MyList("AB")
print(myl2)
print(len(myl2))  # 5