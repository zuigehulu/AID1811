# abs_overwrite.py

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __len__(self):
        '''此方法必须返回整数'''
        return self.data.__len__()
        # return len(self.data)

    def __abs__(self):
        L = [abs(x) for x in self.data]
        lst = MyList(L)  # 创建 MyList类型的新列表 
        return lst

myl = MyList([1, -2, 3, -4, 5])
myl2 = abs(myl)
print(myl)  # MyList([1, -2, 3, -4, 5])
print(myl2)  # MyList([1, 2, 3, 4, 5])
