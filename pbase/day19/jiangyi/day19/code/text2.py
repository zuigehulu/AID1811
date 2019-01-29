class MyList:
    def __init__(self,L):
        self.L = [x for x in L]
    def __repr__(self):
        return "MyList(%s)"%self.L
    def __abs__(self):
        l = [abs(x) for x in self.L]
        lst = MyList(l)
        return lst

myl = MyList([1, -2, 3, -4, 5])
myl2 = abs(myl)
print(myl)  # MyList([1, -2, 3, -4, 5])
print(myl2)  # MyList([1, 2, 3, 4, 5])