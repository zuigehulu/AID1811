# bool.py

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    # def __len__(self):
    #     '''此方法必须返回整数'''
    #     print("__len__方法被调用!")
    #     return len(self.data)

    # def __bool__(self):
    #     print("__bool__ 被调用!!!")
    #     for x in self.data:
    #         if bool(x) == False:
    #             return False
    #     return True


myl = MyList([1, 0, 3, 0, 5])

print(bool(myl))  # ??
if myl:  # <<<--- 相当于 if bool(myl)
    print("真值")
else:
    print("假值")